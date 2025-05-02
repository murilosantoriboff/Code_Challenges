#include <stdio.h>

void main(){
    int num, soma;
    int d1, d2, d3, d4;
    printf("Escreva um valor de 5 digitos par ver a soma deles:\n");
    scanf("%d", &num);
    d1 = num /1000;
    d2 = (num /100) % 10;
    d3 = (num /10) % 10;
    d4 = num % 10;

    soma = d1 + d2 + d3 + d4;
    printf("Soma: %d\n", soma);
}
