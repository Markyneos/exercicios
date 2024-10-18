#include <stdio.h>

int main(void)
{
  float metros = 1, centimetros;
  printf("Digite um valor para ser convertido de metros para centímetros: ");
  do
    {
      scanf("%f", &metros);
      if (metros < 1)
      {
        printf("Digite um valor válido!\n");
      }
    }
  while (metros < 1);
  centimetros = metros * 100;
  printf("O valor %.2f é, em centímetros: %.2f\n", metros, centimetros);
  return 0;
}