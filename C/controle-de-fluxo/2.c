/*Fazer um programa em "C" que lê o preço de um produto e inflaciona esse
preço em 10% se ele for menor que 100 e em 20% se ele for maior ou igual a
100.
OBS: não use o comando "if" ou o operador de condição "?".*/

#include <stdio.h>

int main(void)
{
    float valor, inflacionado;
    printf("Digite o preço de um produto: ");
    scanf("%f", &valor);
    inflacionado = valor * (1.1 + 0.1 * (valor >= 100));
    printf("Preço inflacionado: R$%.2f\n", inflacionado);
    return 0; 
}