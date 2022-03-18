section .data
  leap: dw "The year is leap"
  leapL: equ $-leap
  notLeap: dw "The year is not leap"
  notleapL: equ $-notLeap
  year: dd 2021
  
section .text
	global _start

_start:
    mov rcx, 0
    mov rax, year
    mov rbx, 4
    div rbx
    mov rdx, rcx
    cmp rdx, 0
    
    mov rsi, rax
    mov [var], rsi
    call printNumber
    call exit

nextDivision:
    mov rcx, 0
    mov rax, year
    mov rbx, 100
    div rbx
    mov rdx, rcx
    cmp rdx, 0
    je nextDivision1
    jne Leap
    call exit

nextDivision1:
    mov rcx, 0
    mov rax, year
    mov rbx, 400
    div rbx
    mov rdx, rcx
    cmp rdx, 0
    je Leap
    jne NotLeap
    call exit
    
Leap:
    mov eax, 4
	  mov ebx, 1
	  mov ecx, leap
	  mov edx, leapL
	  int 0x80
	  jmp exit

NotLeap:
    mov eax, 4
	  mov ebx, 1
	  mov ecx, notLeap
	  mov edx, notleapL
	  jmp exit

exit:
    mov rax, 1
	  mov rbx, 0
	  int 80h;