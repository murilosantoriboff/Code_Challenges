#include <stdio.h>

void main(){
    int tipo_v, h, m, h2, m2;
    int val_car=0, val_mot=0, tot_car=0, tot_mot=0, h_car=0, h_mot=0, m_car=0, m_mot=0;
    printf("Escreva o veiculo, digite -1 para parar!\n");
    while (1) {
        printf("(1- Carro 2- Moto): ");
        scanf("%i",&tipo_v);
        if (tipo_v == -1){
            break;
        }
        while (tipo_v != 1 && tipo_v != 2){
            printf("Valor Errado!! Digite novamente\n");
            printf("(1- Carro 2- Moto): ");
            scanf("%i",&tipo_v);
        }
        printf("Digite hora e minuto de entrada (HH:MM)\n");
        printf("Hora: ");
        scanf("%i",&h);
        printf("Minuto: ");
        scanf("%i",&m);
        while ((h > 24 || h < 0) || (m > 60 || m < 0)) {
            printf("Valor Errado!! Digite novamente\n");
            printf("Digite hora e minuto de entrada (HH:MM)\n");
            printf("Hora: ");
            scanf("%i",&h);
            printf("Minuto: ");
            scanf("%i",&m);
        }
        printf("Digite hora e minuto de saida (HH:MM)\n");
        printf("Hora: ");
        scanf("%i",&h2);
        printf("Minuto: ");
        scanf("%i",&m2);
        while ((h2 > 24 || h2 < 0) || (m2 > 60 || m2 < 0)) {
            printf("Valor Errado!! Digite novamente\n");
            printf("Digite hora e minuto de saida (HH:MM)\n");
            printf("Hora: ");
            scanf("%i",&h2);
            printf("Minuto: ");
            scanf("%i",&m2);
        }
        printf("-----------------------------------------\n");
        if (tipo_v == 1){
            if((h2-h == 0) && (m2-m <=30)){
                tot_car += 5;
            }
            else if ((h2-h == 0) && (m2-m <=60)){
                tot_car += 8;
            }
            else {
                h_car = h2-h;
                m_car = m2-m;
                if(m_car > 0){
                    h_car =+ 1;
                }
                tot_car  = h_car*2;

            }
            // Verificar ate 1h e hora adicional
            if(tot_car  >= val_car){
                val_car = tot_car;
            }
        } else if (tipo_v == 2){
            if((h2-h == 0) && (m2-m <=30)){
                tot_mot += 3;
            }
            else if ((h2-h == 0) && (m2-m <=60)){
                tot_mot += 5;
            }
            else {
                h_mot = h2-h;
                m_mot = m2-m;
                if(m_mot > 0){
                    h_mot =+ 1;
                }
                tot_mot = h_mot*1;

            }
            // Verificar ate 1h e hora adicional
            if(tot_mot >= val_mot){
                val_mot = tot_mot;
            }
        }

    }

    printf("Maior valor carro: %i\n",val_car);
    printf("Maior valor moto: %i",val_mot);
}
