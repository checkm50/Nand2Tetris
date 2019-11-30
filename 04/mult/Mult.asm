// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Multiplies R0 and R1 and stores the result in R2
//(R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//i = 0
//n = R1
//basenumber = b = R0

//LOOP:
//if i >= n goto END
//    i = i+R0
//    goto LOOP

//END:
//    goto END 


// initialize i to 0
@i
M=0

//initialize R2 to 0
@R2
M=0

//n = R1
@R1
D=M
@n
M=D

//basenumber = b = R0
@R0
D=M
@b
M=D

//R0 = b = 3
//R1 = n = 1
//i = 0


    @b
    D=M
    @STOP
    D;JEQ

    @n
    D=M
    @STOP
    D;JEQ

(LOOP)
    
    @i
    D=M // D=0
    @b
    D=D+M // D=3
    @i
    M=D // i=3
    @n
    D=M-1 // D= 0
    @n
    M=D //Updating n
    @LOOP
    D;JGT //if n > 0
    @STOP
    0;JMP 

(STOP)
@i
D=M
@R2
M=D //RAM[2] = i

(END)
@END
0;JMP