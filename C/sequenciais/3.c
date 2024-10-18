#include <stdio.h>

int main(void)
{
    int numero;
    printf("Digite um número: ");
    scanf("%d", &numero);
    
    printf("Decimal: %d\nHexadecimal: %X\nOctal: %o\n", numero, numero, numero);
    return 0;
}