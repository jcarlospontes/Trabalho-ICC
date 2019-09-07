# Trabalho-ICC

Programa feito para a cadeira de introdução à computação 2018.2

Tema: Agenda telefônica

Objetivo: Implemente um programa que controla uma lista de
nomes e telefones, com opções para exibir todos os itens, incluir, alterar, excluir e
pesquisar por nome ou por telefone. Os dados devem ser armazenados em arquivo
para possibilitar que sejam mantidos em caso de encerramento do programa.

Exemplo de descrição de circuito:


% Linhas iniciando com % são linhas de comentários.

% Circuito 1 - Somador completo

% Parte 1: dados quantitativo de ids do circuito.

n_entr,3,Cin,A,B

n_said,2,S,Cout

n_gate,5,gi,g2,g3,g4,g5

% Parte 2 da descrição: interconexões (ID do gate,tipo, saída, lista de entradas; y1 é a saída do gate g1).

g1,xor,y1,A,B

g2,xor,S,y1,Cin

g3,and,y3,y1,Cin

g4,and,y4,B,A

g5,or,Cout,y3,y4
