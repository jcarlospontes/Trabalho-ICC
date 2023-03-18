#include <stdio.h>
#include <stdlib.h>
#include "MatrizDinamica.h"
#include "MatrizDinamica.c"

int main(){

int m,n,e;

printf("\nDigite o numero de linhas da matriz: ");
scanf("%d",&m);
printf("Digite o numero de colunas da matriz: ");
scanf("%d",&n);

int **matriz = criar_matriz(m,n);

preenche_matriz(matriz, m, n);

while(1){
    printf("\nO que deseja fazer? 1(imprimir matriz) 2(criar outra matriz) 3(sair) ");
    scanf("%d",&e);

    switch(e){
        case 1:
            imprime_matriz(matriz, m, n);
            continue;
        case 2:
            libera_matriz(matriz,m);
            printf("\nDigite o numero de linhas da matriz: ");
            scanf("%d",&m);
            printf("Digite o numero de colunas da matriz: ");
            scanf("%d",&n);
            int **matriz = criar_matriz(m,n);
            preenche_matriz(matriz, m, n);
            continue;
        default:
            break;
    }
    if((e != 1) || (e != 2)){
        break;
    }
}


libera_matriz(matriz,m);


return 0;
}