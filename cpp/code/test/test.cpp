void add_overflow_test()
{
    char x = 0xff;    // 0x000000318FF9FB70 ff
    char y = 0x01;    // 0x000000318FF9FB71 01
    char z = x + y;   // 0x000000318FF9FB72 00
    return;
}

int main()
{
    add_overflow_test();
    return 0;
}
