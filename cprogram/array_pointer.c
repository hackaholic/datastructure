#include<stdio.h>

int main() {

    //array a of type integer
    int a[5] = {10, 20, 30, 40, 50};
    printf("Index, value using index, value using pointer, address using pointer, address using index\n");
    for(int i=0; i<5; i++){
        printf("%d, %d, %d, %u, %u, %p\n", i, a[i], *(a+i), a+i, &a[i], a+i);
    } 

    return 0;
}
