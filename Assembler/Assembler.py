from termcolor import colored
#print(colored('Hello, World!', 'green'))
outfileWOcmntandblank = open('outfileWOcmntandblank.out','w')
outfileWOlabel = open('outfileWOlabel.out','w')
outfileWOsymbol = open('outfileWOsymbol.hack','w')
symbolTable = {
                'SP': 0,
                'LCL': 1,
                'ARG': 2,
                'THIS': 3,
                'THAT': 4,
                'R0': 0,
                'R1': 1,
                'R2': 2,
                'R3': 3,
                'R4': 4,
                'R5': 5,
                'R6': 6,
                'R7': 7,
                'R8': 8,
                'R9': 9,
                'R10': 10,
                'R11': 11,
                'R12': 12,
                'R13': 13,
                'R14': 14,
                'R15': 15,
                'SCREEN': 16384,
                'KBD:': 24576
                }
variableIndexSymbol = 16
zerocomp = {
            '0': '101010',
            '1': '111111',
            '-1': '111010',
            'D': '001100',
            'A': '110000',
            '!D': '001101',
            '!A': '110001',
            '-D': '001111',
            '-A': '110011',
            'D+1': '011111',
            'A+1': '110111',
            'D-1': '001110',
            'A-1': '110010',
            'D+A': '000010',
            'D-A': '010011',
            'A-D': '000111',
            'D&A': '000000',
            'D|A': '010101'
}
onecomp = {
            'M': '110000',
            '!M': '110001',
            '-M': '110011',
            'M+1': '110111',
            'M-1': '110010',
            'D+M': '000010',
            'D-M': '010011',
            'M-D': '000111',
            'D&M': '000000',
            'D|M': '010101'
}

dest = {
            'null': '000',
            'M': '001',
            'D': '010',
            'MD': '011',
            'A': '100',
            'AM': '101',
            'AD': '110',
            'AMD': '111',
}

jmp = {
            'null': '000',
            'JGT': '001',
            'JEQ': '010',
            'JGE': '011',
            'JLT': '100',
            'JNE': '101',
            'JLE': '110',
            'JMP': '111',
}


def printToFile(handle, line):
    handle.write(line)

def convert2binary(input):
    convertedvalue = f'{int(input):015b}'
    return convertedvalue

if __name__ == "__main__":
    with open('assemblycode.txt') as f:
        for line in f:
            # Remove empty lines
            if line == "\n":
                continue

            try:
                # Remove comments
                commentIndex = line.index('//')
                if(commentIndex == 0):
                    continue
                elif(commentIndex >= 0):
                    line = line[:commentIndex]
                    printToFile(outfileWOcmntandblank, line)
            except ValueError:
                printToFile(outfileWOcmntandblank, line)
    outfileWOcmntandblank.close()

    with open('outfileWOcmntandblank.out') as f:
        lineNum = 0
        for line in f:        
            # First pass. Find all (xxx) and put them in symbol table
            try:
                labelStartIndex = line.index('(')
                if(labelStartIndex >= 0):
                    labelEndIndex = line.index(')')
                    labelToLoad = line[labelStartIndex+1:labelEndIndex]
                    symbolTable[labelToLoad] = lineNum
                    #print(symbolTable)
            except ValueError:
                printToFile(outfileWOlabel, line)
                lineNum+=1
    outfileWOlabel.close()

    # Second pass
    with open('outfileWOlabel.out') as pass2F:
        for line in pass2F:
            try:
                line = line.strip()
                addressInsLine = line.index('@')
                if(addressInsLine >= 0):
                    addressInstruction = line[addressInsLine+1:]
                    if(addressInstruction.isnumeric()):
                        addressInstruction = convert2binary(addressInstruction)
                        printToFile(outfileWOsymbol, '0' + str(addressInstruction) + '\n')
                    elif(addressInstruction not in symbolTable):
                        symbolTable[addressInstruction] = variableIndexSymbol
                        output = convert2binary(variableIndexSymbol)
                        printToFile(outfileWOsymbol, '0'+ str(output) + '\n')
                        variableIndexSymbol+=1
                    elif(addressInstruction in symbolTable):
                        output = convert2binary(symbolTable[addressInstruction])
                        printToFile(outfileWOsymbol, '0'+ str(output) + '\n')
                    else:
                        continue
            except ValueError:
                print('Processing comp statements: ', line)
                # 111 are the start bits (MSB)
                compMSB_bits = '111'
                line = line.strip()
                try:
                    if(line.find('=') >= 0):
                        #processing with dest
                        destAndcomp = line.split('=')
                        destination = destAndcomp[0]
                        comp = destAndcomp[1]
                        destination_bits = dest[destination]
                        if(comp in zerocomp):
                            comp_bits = '0' + zerocomp[comp]
                        else:
                            comp_bits = '1' + onecomp[comp]
                        jmp_bits = jmp['null']
                        comp_instruction_bits = compMSB_bits + comp_bits + destination_bits + jmp_bits
                    elif(line.find(';') >= 0):
                        #processing jmp
                        compAndjmp = line.split(';')
                        comp = compAndjmp[0]
                        jmp_bits = compAndjmp[1]
                        destination_bits = dest['null']
                        if(comp in zerocomp):
                            comp_bits = '0' + zerocomp[comp]
                        else:
                            comp_bits = '1' + onecomp[comp]
                        jmp_bits = jmp[jmp_bits]
                        comp_instruction_bits = compMSB_bits + comp_bits + destination_bits + jmp_bits
                    else:
                        pass
                    printToFile(outfileWOsymbol, comp_instruction_bits + '\n')
                except ValueError:
                    print(colored('Unknown instruction ..', 'red'))

    outfileWOsymbol.close()     

