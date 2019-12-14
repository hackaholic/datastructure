#include<stdio.h>

// sum of array element using pointer post increment
int main(){
    
    int a[5] = {10, 20, 30, 40, 50};
    int *p = a;
    int sum = 0;
    for(int i=0; i<5; i++){
        sum += *p;
	p++;
    }
    printf("Sum of array element {10, 20, 30, 40, 50} : %d\n", sum);
    return 0;
}
