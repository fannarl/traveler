int getByte(int x, int n) {
    int x = 0x12345678;
    int n = 1;
    return (x >>(n<<3)) & 0xff;
