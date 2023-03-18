#include <stdio.h>
#include <stdlib.h>
#include "Cilindro.h"
#include "Cilindro.c"

int main(){

float r,h,a,v;

Cilindro* cilindro;

printf("\nDigite a altura do cilindro: ");
scanf("%f",&h);
printf("Digite o raio do cilindro: ");
scanf("%f",&r);

cilindro = criar_cilindro(r,h);

printf("\n\nArea do cilindro criado: %f\n\n",retorna_area_cilindro(cilindro));

printf("Volume do cilindro criado: %f",retorna_volume_cilindro(cilindro));


liberar_cilindro(cilindro);

return 0;
}



