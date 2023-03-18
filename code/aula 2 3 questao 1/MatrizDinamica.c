#include <stdlib.h>
#include <stdio.h>
#include "MatrizDinamica.h"

int **criar_matriz(int linha, int coluna){
    int cont = 0;
    int **matriz = malloc(linha * sizeof(int *));
    while(cont < linha){
        matriz[cont] = malloc(coluna * sizeof(int*));
        cont++;
    }
    return matriz;
}

void libera_matriz(int **matriz, int linha){
    int cont = 0;
    while(cont < linha){
        free(matriz[cont]);
        cont++;
    }
    free(matriz);
}

void imprime_matriz(int **matriz, int linha, int coluna){
    printf("\nImprimindo a matriz:\n\n");
    for(int x = 0; x < linha; x++){
        for(int y = 0; y< coluna; y++){
            printf("%d ", matriz[x][y]);
            if(y == (coluna-1)){
                printf("\n");
            }
        }
    }
}

void preenche_matriz(int **matriz, int linha, int coluna){
    printf("\nPreencha a matriz:\n\n");
    for(int x = 0; x < linha; x++){
        for(int y = 0; y< coluna; y++){
            printf("Celula [%d][%d]: ",x, y);
            scanf("%d", &matriz[x][y]);
        }
    }
}