#include <stdio.h>
#include <math.h>

int main(void)
{
  float raio, area;
  printf("Digite o raio de um círculo para cálculo de sua área(cm ou m): ");
  scanf("%f", &raio);
  while (raio < 1)
    {
      printf("Digite um número válido!\n");
      printf("Digite o raio de um círculo para cálculo de sua área: ");
      scanf("%f", &raio);
    }
  if (raio == 0)
  {
    printf("O programa está sendo fechado\n");
    return 0;
  }
  else
  {
    area = M_PI * (raio * raio);
    printf("A área do círculo de raio %f é, aproximadamente, %.2f\n", raio, area);
    return 0;
  }
}