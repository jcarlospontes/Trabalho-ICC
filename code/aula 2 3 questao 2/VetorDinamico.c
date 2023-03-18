#include <stdlib.h>
#include <stdio.h>
#include "VetorDinamico.h"

int **criar_vetor(int tamanho){
    int cont = 0;
    int **vetor = malloc(tamanho * sizeof(int *));
    return vetor;
}

void libera_vetor(int **vetor, int tamanho){
    int cont = 0;
    while(cont < tamanho){
        free(vetor[cont]);
        cont++;
    }
    free(vetor);
    printf("\nLiberando o vetor da memoria.\n");
}

void imprime_vetor(int **vetor,int tamanho){
    printf("\nImprimindo a matriz:\n\n");
    for(int x = 0; x < tamanho; x++){
        printf("%d ", vetor[x]);
        if(x == (tamanho-1)){
            printf("\n");
        }
    }
}

void preenche_vetor(int **vetor, int tamanho){
    printf("\nPreencha o vetor:\n\n");
    for(int x = 0; x < tamanho; x++){
        printf("Celula [%d]: ",x);
        scanf("%d", &vetor[x]);
    }
}