#include<stdio.h>

int main() {
    int x;
    int *p;
    p = &x;
    printf("Enter a number:");
    scanf("%d", p);
    printf("Value: %d, Address: %p, Value using pointer: %d\n", x, p, *p);
    return 0;
}
