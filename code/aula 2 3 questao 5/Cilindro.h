typedef struct cilindro Cilindro;

Cilindro* criar_cilindro(float raio, float altura);

void liberar_cilindro(Cilindro* cilindro);

float retorna_altura_cilindro(Cilindro* cilindro);

float retorna_raio_cilindro(Cilindro* cilindro);

void seta_atributo_cilindro(Cilindro* cilindro, float raio, float altura);

float retorna_area_cilindro(Cilindro* cilindro);

float retorna_volume_cilindro(Cilindro* cilindro);

