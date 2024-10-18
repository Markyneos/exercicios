#include <stdio.h>

int main(void)
{
    float valor = 0.0;
    printf("Digite um valor em metros para transformá-lo: ");
    scanf("%f", &valor);
    printf("Metro: %.2f\nDecímetro: %.2f\nCentímetro: %.2f\nMilímetro: %.3f\n", valor, valor / 10, valor / 100, valor / 1000);
    return 0;
}