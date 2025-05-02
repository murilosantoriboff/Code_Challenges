#include <stdio.h>

void main(){

    int n, soma, fat=1, i;

    printf("Write a number: ");
    scanf("%i", &n);

    for(i=1; i<=n; i++){
        fat *= i;
        soma += 1/fat;

    }

    soma += 1;
    printf("Valor of E: %i",soma);
}
