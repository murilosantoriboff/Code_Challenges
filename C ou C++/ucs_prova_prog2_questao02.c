#include <stdio.h>

void main(){

    int n, i;
    float soma=1;

    printf("Write N: ");
    scanf("%i",&n);

    for(i=0;i<=n;i++){
        soma += 1/i;
    }


    printf("Value of the sequence: %i",soma);
}
