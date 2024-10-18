#include <stdio.h>

int main(void)
{
  float notas[4];
  printf("Escreva as 4 notas bimestrais: ");
  scanf("%f %f %f %f", &notas[0], &notas[1], &notas[2], &notas[3]);
  float soma = 0;
  for (int i = 0; i < 4; i++)
    {
      soma += notas[i];
    }
  float media = soma / 4;
  printf("A média das notas bimestrais é: %.2f\n", media);
  return 0;
}