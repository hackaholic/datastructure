#include<stdio.h>

int main() {
    float a = 10.10;
    void *p;

    p = (float *)&a;
    printf("%f\n", *((float *)p));
    return 0;
}
