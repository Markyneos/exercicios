/*Fazer um programa em "C" que solicite 2 números e informe:
 a) A soma dos números;
 b) O produto do primeiro número pelo quadrado do segundo;
 c) O quadrado do primeiro número;
 d) A raiz quadrada da soma dos quadrados;
 e) O seno da diferença do primeiro número pelo segundo;
 f) O módulo do primeiro número.*/

#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main(void)
{
    int num1, num2;
    printf("Digite dois números: ");
    scanf("%i %i", &num1, &num2);
    printf("a) %i\n", num1 + num2);
    printf("b) %.0f\n", num1 * pow(num2, 2));
    printf("c) %.0f\n", pow(num1, 2));
    printf("d) %.2f\n", sqrt(pow(num1, 2) + pow(num2, 2)));
    printf("e) %.2f\n", sin(num1 - num2));
    printf("f) %i\n", abs(num1));
    return 0;
}