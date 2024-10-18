#include <stdio.h>

#define ANSI

#ifdef KR
int soma();
int subtracao();
#else
int soma(int a, int b);
int subtracao(int a, int b);
#endif

int main(void)
{
    int num1, num2;

    printf("Digite o primeiro número: ");
    scanf("%i", &num1);
    printf("Digite o segundo número: ");
    scanf("%i", &num2);

    printf("Soma: %d\n", soma(num1, num2));
    printf("Subtração: %d\n", subtracao(num1, num2));

    return 0;
}

#ifdef KR
int soma(a, b)
int a, b;
{
    return a + b;
}

int subtracao(a, b)
int a, b;
{
    return a - b;
}

#else
int soma(int a, int b)
{
    return a + b;
}
int subtracao(int a, int b)
{
    return a - b;
}
#endif