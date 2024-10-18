/*Fazer um programa que lê um valor, um operador (+,-,*,/) e outro valor e
imprime o resultado da expressão:
 <valor 1> <operador> <valor 2>*/
#include <stdio.h>

int main(void)
{
    int valor1, valor2, escolha;
    char operacoes[4] = {'+', '-', 'x', '/'};
    printf("Escolha uma operação:\n(1) Adição\n(2) Subtração\n(3) Multiplicação\n(4) Divisão\n");
    scanf("%i", &escolha);
    printf("Digite primeiro número: ");
    scanf("%i", &valor1);
    printf("Digite segundo número: ");
    scanf("%i", &valor2);

    switch (escolha)
    {
    case 1:
        printf("%i %c %i = %i\n", valor1, operacoes[escolha - 1], valor2, valor1 + valor2);
        break;
    case 2:
        printf("%i %c %i = %i\n", valor1, operacoes[escolha - 1], valor2, valor1 - valor2);
        break;
    case 3:
        printf("%i %c %i = %i\n", valor1, operacoes[escolha - 1], valor2, valor1 * valor2);
        break;
    case 4:
        printf("%i %c %i = %i\n", valor1, operacoes[escolha - 1], valor2, valor1 / valor2);
        break;
    }
    return 0;
}