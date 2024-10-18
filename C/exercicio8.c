#include <stdio.h>

int main(void)
{
  float sal_hora;
  int horas;
  printf("Digite o número o seu ganho por hora e o número de horas trabalhadas no mês: ");
  scanf("%f %i", &sal_hora, &horas);
  while (sal_hora < 1 || horas < 1)
    {
      printf("Digite valores válidos!\n");
      printf("Digite o número o seu ganho por hora e o número de horas trabalhadas no mês: ");
      scanf("%f %i", &sal_hora, &horas);
    }
  float salario = sal_hora * horas;
  printf("Seu salário é de R$%.2f\n", salario);
  return 0;
}