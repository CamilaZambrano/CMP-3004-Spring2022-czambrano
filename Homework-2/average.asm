section .data
  array: db 2, 1, 3, 1, 2
  
section .text
    global _start

_start:
    mov rax, [array]
    mov rsi, 0
 
 loop: 
    mov rdx, [array+rsi]
    add rax, rdx
    inc rsi
    cmp rsi, 4	
    jne loop
		
    mov rbx, rax
    mov rcx, 5
    div rbx, rcx
    
    mov rax, 1
    mov rbx, 0
    int 80h;