/*Faça um programa em "C" que lê dois valores e imprime:
 - se o primeiro valor for menor que o segundo, a lista de valores do primeiro até
o segundo;
 - se o primeiro valor for menor que o segundo a lista de valores do segundo até
o primeiro em ordem decrescente;
 - se ambos forem iguais a mensagem "valores iguais".*/

#include <stdio.h>

int main(void)
{
    int v1, v2;
    printf("Digite dois valores: ");
    scanf("%i %i", &v1, &v2);
    if (v1 == v2)
    {
        printf("Valores iguais\n");
    }
    else if (v1 < v2)
    {
        int diferenca = v2 - v1;
        for (int i = 0; i <= diferenca; i++)
        {
            printf("%i ", v1 + i);
        }
        printf("\n");
        for (int i = 0; i <= diferenca; i++)
        {
            printf("%i ", v2 - i);
        }
        printf("\n");
    }
    return 0;
}