#include <stdio.h>
#include "TADPessoa.h"

void receberDados (Pessoa *p){
	strcpy(p->nome, "Vinicius");
	p->diaNascimento = 22;
	p->mesNascimento = 10;
	p->anoNascimento = 1990;
	strcpy(p->CPF, "351.687.363-99");
}

void imprimirPessoa (Pessoa *p){
	printf("Nome: %s \nData de Nascimento: %d/%d/%d \nCPF: %s ", p->nome, p->diaNascimento, p->mesNascimento, p->anoNascimento, p->CPF);
	printf("\n");
}
