#include <stdio.h>

void main(){

    int senha, senha2, i;
    for(i=0;i<=10;i++){

        scanf("%i",&senha);
        scanf("%i",&senha2);
        while(senha != senha2){
            scanf("%i",&senha2);
        }
        printf("Welcome!\n");
    }
}
