/*Fazer uma função que cacula a enésima potência de uma variável real x:
f(x, n) = xn*/

#include <stdio.h>

int potencia(int num, int expoente);

int main(void)
{
    int expoente = 0;
    int numero = 0;
    printf("Digite o número que você deseja elevar: ");
    scanf("%i", &numero);
    printf("Digite seu expoente: ");
    scanf("%i", &expoente);

    printf("O número %i elevado a %i é igual a: %i\n", numero, expoente, potencia(numero, expoente));
    return 0;
}
int potencia(int num, int expoente)
{
    int potencia = num;
    if (expoente == 0)
    {
        return 1;
    }
    else if (expoente == 1)
    {
        return num;
    }
    for (int i = 1; i < expoente; i++)
    {
        potencia *= num;
    }
    return potencia;
}