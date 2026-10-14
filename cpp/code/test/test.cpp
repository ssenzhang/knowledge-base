#include <climits>

void add_overflow_test()
{
    char x = 0xff;    // 0x000000D8E054F720 ff
    char y = 0x02;    // 0x000000D8E054F721 02
    char z = x + y;   // 0x000000D8E054F722 01 00

    int xmax = INT_MAX;      // 0x000000D8E054F724 ff ff ff 7f
    int xmin = INT_MIN;      // 0x000000D8E054F728 00 00 00 80
    int negxmin = -INT_MIN;  // 0x000000D8E054F72C 00 00 00 80

    return;
}

int main()
{
    add_overflow_test();
    return 0;
}
