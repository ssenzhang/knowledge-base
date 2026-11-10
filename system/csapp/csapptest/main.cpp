#include <cassert>
#include <iostream>

#if defined(_WIN64)
extern "C" long asm1(long *xp, long *yp, long *zp);
#else
long asm1(long *xp, long *yp, long *zp)
{
    long result;
    __asm {
        mov eax, xp
        mov ecx, [eax]       ; x
        mov eax, yp
        mov edx, [eax]       ; y
        mov eax, zp
        mov eax, [eax]       ; z
        mov result, eax

        mov eax, yp
        mov [eax], ecx       ; *yp = x
        mov eax, zp
        mov [eax], edx       ; *zp = y
        mov eax, xp
        mov ecx, result
        mov [eax], ecx       ; *xp = z
    }
    return result;
}
/**
AT&T
.globl asm1
asm1:
    movq (%rdi), %r8
    movq (%rsi), %rcx
    movq (%rdx), %rax
    movq %r8, (%rsi)
    movq %rcx, (%rdx)
    movq %rax, (%rdi)
    ret
*/
#endif

long asm1_c(long *xp, long *yp, long *zp)
{
    long x = *xp;
    long y = *yp;
    long z = *zp;
    *yp = x;
    *zp = y;
    *xp = z;
    return z;
}
int main()
{
    long x = 1, y = 2, z = 3;
    long x1 = 1, y1 = 2, z1 = 3;
    assert(asm1(&x, &y, &z) == asm1_c(&x1, &y1, &z1) && "asm1 and asm1_c are not equal");
    assert(x1 == 3 && y1 == 1 && z1 == 2 && "x1, y1, z1 are not equal to 3, 1, 2");
    assert(x == x1 && y == y1 && z == z1 && "x, y, z are not equal to 1, 2, 3");
    std::cout << "[PASS] asm1 test passed!" << std::endl;

    return 0;
}