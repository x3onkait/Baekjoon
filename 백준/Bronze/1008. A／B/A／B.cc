#include <stdio.h>

int main(void){

    int first, second;
    scanf("%d %d", &first, &second);

    printf("%.9f", (double)first / (double)second);

    return 0;

}