/*Fazer um programa em "C" que lê 10 valores e imprime o maior e o menor
valores lidos.*/

#include <stdio.h>

int main(void)
{
    int numeros[10];
    printf("Digite 10 valores\n");
    for (int i = 0; i < 10; i++)
    {
        printf("Digite o número %i: ", i + 1);
        scanf("%i", &numeros[i]);
    }
    int menor = numeros[0];
    int maior = numeros[9];
    
    for (int i = 0; i < 10; i++)
    {
        if (menor > numeros[i])
        {
            menor = numeros[i];
        }
        if (maior < numeros[i])
        {
            maior = numeros[i];
        }
    }
    printf("Maior número: %i\nMenor número: %i\n", maior, menor);
    return 0;
}