#include <stdio.h>
#include <stdlib.h>
#include "VetorDinamico.h"
#include "VetorDinamico.c"

int main(){

int n,e;

printf("\nDigite o tamanho do vetor: ");
scanf("%d",&n);

int **vetor = criar_vetor(n);

preenche_vetor(vetor, n);

imprime_vetor(vetor, n);

libera_vetor(vetor,n);


return 0;
}