// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

// Keyboard address
@KBD
D=A
@kbdaddress
M=D

// Screen address
@SCREEN
D=A
@scrnaddress
M=D

// kbdstartaddress - screenstartaddress gives entires area to fill-up
@kbdaddress
D = M - 1
@scrnaddress
D = D - M
@endofloop
M = D

(KEYBOARDCAPTURE)
@KBD
D = M
@WHITE
D;JEQ
@BLACK
0;JMP


(WHITE)
    @endofloop
    D = M
    @i
    M = D
    (WHITELOOP)
        
        @i
        D = M
        @KEYBOARDCAPTURE
            D;JLT
        @scrnaddress
        D = M
        @i
        D = D + M
        A = D
        M=0
        @i
        M = M - 1
        @WHITELOOP
        0;JMP

(BLACK)
    @endofloop
    D = M
    @i
    M = D
    (BLACKLOOP)
        
        @i
        D = M
        @KEYBOARDCAPTURE
            D;JLT
        @scrnaddress
        D = M
        @i
        D = D + M
        A = D
        M=-1
        @i
        M = M - 1
        @BLACKLOOP
        0;JMP

(END)
@END
0;JMP

























