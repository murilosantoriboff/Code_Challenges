#include <stdio.h>;
#include <math.h>;

void main(){
    int num_bin, decimal;
    int d1, d2, d3, d4, d5, d6;
    printf("Escreva um numero decimal de até 6 digitos para ver seu decimal: ");
    scanf("%d", &num_bin);
    d1 = num_bin /100000;
    num_bin = num_bin % 100000;
    d2 = num_bin /10000;
    num_bin = num_bin % 10000;
    d3 = num_bin /1000;
    num_bin = num_bin % 1000;
    d4 = num_bin /100;
    num_bin = num_bin % 100;
    d5 = num_bin /10;
    d6 = num_bin % 10;

    decimal = d6 + d5*2 + d4*4 + d3*8 + d2*16 + d1*32;

    printf("Decimal: %d\n", decimal);
};
