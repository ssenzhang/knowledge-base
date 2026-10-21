#include <iostream>
#include <iomanip>

void show_bytes(void *start, size_t len)
{
    for (unsigned i = 0; i < len; i++)
    {
        std::cout << std::setw(2) << std::setfill('0') << std::hex << (unsigned)((unsigned char*)start)[i] << " ";
    }
    std::cout << std::endl;
}

bool is_little_endian()
{
    short one = 1;
    return ((unsigned char*)&one)[0];
}

void hwk_5_59()
{
    int x = 0x89ABCDEF;
    int y = 0x76543210;

    std::cout << std::hex <<((x & 0xFF) | (y & ~0xFF)) << std::endl;
}

unsigned replace_byte(unsigned x, int i, unsigned char b)
{
    return (x & ~(0xFF << (i * sizeof(unsigned)))) | (b << (i * sizeof(unsigned)));
}

unsigned char get_msb(int x)
{
    return (x  >> ((sizeof(int) - 1) << 3)) & 0xff;
}

int main()
{
    short one = 1;
    short sx = 0x12345;
    int i = 0x12345;
    long l = 0x12345;
    long long ll = 0x12345;
    float f = 0x12345;
    double d = 0x12345;

    std::cout << (((unsigned char*)&one)[0] ? "little endian" : "big endian") << std::endl;
    show_bytes((void*)&one, sizeof(one));
    show_bytes((void*)&sx, sizeof(sx));
    show_bytes((void*)&i, sizeof(i));
    show_bytes((void*)&l, sizeof(l));
    show_bytes((void*)&ll, sizeof(ll));
    show_bytes((void*)&f, sizeof(f));
    show_bytes((void*)&d, sizeof(d));

    hwk_5_59();

    std::cout << std::hex << replace_byte(0x12345678, 2, 0xAB) << std::endl;
    std::cout << std::hex << replace_byte(0x12345678, 0, 0xAB) << std::endl;

    int i2 = 0x1234567;
    show_bytes((void*)&i2, sizeof(i2));
    std::cout << std::setw(2) << std::setfill('0') << std::hex << (unsigned short)get_msb(i2) << std::endl;
}