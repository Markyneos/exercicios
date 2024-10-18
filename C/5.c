#include <stdio.h>

float somaImposto(float taxa, float custo);

int main(void)
{
  float taxa = 0;
  float custo = 0.0;
  printf("Digite a taxa do imposto(%): ");
  scanf("%f", &taxa);
  printf("Digite o preço/custo do produto: ");
  scanf("%f", &custo);

  float novo_valor = somaImposto(taxa, custo);
  printf("O novo valor é R$%.2f\n", novo_valor);
  return 0;
}
float somaImposto(float taxa, float custo)
{
  float novo_valor = ((taxa / 100) * custo) + custo;
  return novo_valor;
}