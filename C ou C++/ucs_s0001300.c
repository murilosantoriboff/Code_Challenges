#include <stdio.h>

void main()
{
    int hi, mi, si, hf, mf, sf;
    int somaI, somaF, soma;

    printf("Escreva 2 horarios (hh,mm,ss) para ver a soma dos segundos:\n");
    scanf("%d%d%d%d%d%d", &hi, &mi, &si, &hf, &mf, &sf);

    somaI = (hi*3600) + (mi*60) + si;
    somaF = (hf*3600) + (mf*60) + sf;
    soma = somaF-somaI;
    printf("A soma dos segundos: %d", soma);
}
