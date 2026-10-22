#include <iostream>
#include <iomanip>

void show_bytes(void *start, size_t len)
{
    for (size_t i = 0; i < len; i++)
    {
        std::cout << std::setw(2) << std::setfill('0') << std::hex << (unsigned short)((unsigned char*)start)[i] << " ";
    }
    std::cout << std::endl;
}

void show_bytes(int x)
{
    show_bytes((void*)&x, sizeof(x));
}

void hwk_2_61(int x)
{
    std::cout << "x: ";
    show_bytes(x);
    std::cout << "any bit of x equals 1: " << !!x << std::endl;
    std::cout << "any bit of x equals 0: " << !!~x << std::endl;
    std::cout << "any bit in the least significant byte of x equals 1: " << !!(x & 0xFF) << std::endl;
    std::cout << "any bit in the most significant byte of x equals 0: " << !!(~(x >> 24) & 0xFF) << std::endl;
}

// 2.62
bool int_shifts_are_arithmetic()
{
    int x = ~0;
    return !(~(x >> 1));
}
bool unsigned_shifts_are_logical()
{
    unsigned int x = ~0;
    return ~(x >> 1);
}

// 2.63
unsigned srl(unsigned x, int k)
{
    /* Perform shift arithmetically */
    unsigned xsra = (int)x >> k;
    unsigned mask1 = ~(~0 << ((sizeof(unsigned) << 3) - k));  // error when k is 0 or 32
    unsigned mask = ((unsigned)2 << (sizeof(unsigned) * 8 - k - 1)) - 1;  // 1…0000 - 1 = 0…1111
    return xsra & mask;
}
int sra(int x, int k)
{
    /* Perform shift logically */
    int xsrl = (unsigned)x >> k;

    int w = sizeof(int) << 3;
    unsigned high = ~(((unsigned)2 << (w - k - 1)) - 1);  // 111...000
    int flag = !(x & (int)(1u << (w - 1))) - 1; // [1,0,...] & x (10.... or 0) -!-> 0 or 1 -> 1,... or 0 
    return xsrl | (high & flag);
}

// 2.64
int any_odd_one(unsigned x)
{
    
}

int main()
{
    hwk_2_61(0xffffffff);
    std::cout << std::endl;
    hwk_2_61(0x00000000);
    std::cout << std::endl;
    hwk_2_61(0x00000011);
    std::cout << std::endl;
    hwk_2_61(0x00100000);

    std::cout << std::endl;
    std::cout << "int_shifts_are_arithmetic: " << int_shifts_are_arithmetic() << std::endl;
    std::cout << "unsigned_shifts_are_logical: " << unsigned_shifts_are_logical() << std::endl;

    std::cout << std::endl;
    std::cout << "srl(0xF0000000, 4): " << std::hex << srl(0xF0000000, 4) << std::endl;
    std::cout << "sra(0xF0000000, 4): " << std::hex << sra(0xF0000000, 4) << std::endl;
}