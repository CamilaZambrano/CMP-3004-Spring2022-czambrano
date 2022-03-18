section .data
  degreeF: db 46
  degreeC: db 9
	
section .text
  global _start

_start:
  mov rax, degreeF
  call farenheit
  mov rbx, degreeC
  call celsius 
  
  mov rax, 1
  mov rbx, 0
  int 80h;
  
farenheit:
  mov rcx, 32
  sub rax, rcx
  mov rdx, 5
  mov rsi, 9
  div rsi, rdx
  mul rsi, rax
  
celsius:
  mov r8, 9
  mov r9, 5
  div r8, r9
  mul r8, rbx
  mov r10, 32
  add rbx, r10