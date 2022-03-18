section .data

section .text
    global _start

_start:
    mov rax, 0
    mov rbx, 1
    mov rcx, 1 
    mov rdx, 1

    loop: 
        mov rbx,rax
        add rax,rcx
        mov rcx,rbx
        inc rdx
        cmp rdx,49
        jne loop
    
    mov rax, 1
    mov rbx, 0
    int 80h;
