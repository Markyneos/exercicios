#include <stdio.h>

int main(void)
{
  float lado, area, dobro;
  do
    {
      printf("Digite o lado de um quadrado: ");
        scanf("%f", &lado);
      if (lado < 1)
      {
        printf("Digite um valor válido!\n");
      }
    }
    while (lado < 1);
  area = lado * lado;
  dobro = area * 2;
  printf("A área do quadrado e seu dobro são, aproximadamente: %.2f e %.2f\n", area, dobro);
  return 0;
}