.code
asm1 PROC
    mov r9, qword ptr [rcx]
    mov r10, qword ptr [rdx]
    mov rax, qword ptr [r8]
    mov qword ptr [rdx], r9
    mov qword ptr [r8], r10
    mov qword ptr [rcx], rax
    ret
asm1 ENDP
END