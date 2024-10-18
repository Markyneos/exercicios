/*Fazer uma função que calcula o fatorial de um número. Implementar uma
versão recursiva e uma versão com laço.*/

#include <stdio.h>

int fatorial_iterativo(int num);
int fatorial_recursivo(int num);

int main(void)
{
    int numero = 0;
    printf("Digite o número que você deseja descobrir o fatorial: ");
    scanf("%i", &numero);
    printf("O fatorial (recursivo) de %i é: %i\n", numero, fatorial_recursivo(numero));
    printf("O fatorial (iterativo) de %i é: %i\n", numero, fatorial_iterativo(numero));
    return 0;
}
int fatorial_iterativo(int num)
{
    int resultado = 1;
    for (int i = num; i > 0; i--)
    {
        resultado *= i;
    }
    return resultado;
}
int fatorial_recursivo(int num)
{
    if (num == 0 || num == 1)
    {
        return 1;
    }
    else
    {
        return num * fatorial_recursivo(num - 1);
    }
}