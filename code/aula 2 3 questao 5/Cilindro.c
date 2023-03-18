#include <stdlib.h>
#include <stdio.h>
#include "Cilindro.h"

struct cilindro{
    float altura;
    float raio;
};

Cilindro* criar_cilindro(float raio, float altura){
    Cilindro* c = malloc(sizeof(Cilindro));
    if(c!= NULL){
        c->raio = raio;
        c->altura = altura;
    }
    return c;
}

void liberar_cilindro(Cilindro* cilindro){
    free(cilindro);
}

float retorna_altura_cilindro(Cilindro* cilindro){
    return cilindro->altura;
}

float retorna_raio_cilindro(Cilindro* cilindro){
    return cilindro->raio;
}

void seta_atributo_cilindro(Cilindro* cilindro, float raio, float altura){
    cilindro->altura = altura;
    cilindro->raio = raio;
}

float retorna_area_cilindro(Cilindro* cilindro){
    float area = (2 * 3.14f * cilindro->raio)*(cilindro->raio + cilindro->altura);
    return area;
}

float retorna_volume_cilindro(Cilindro* cilindro){
    float volume = (3.14f * (cilindro->raio) * (cilindro->raio) * (cilindro->altura));
    return volume;
}