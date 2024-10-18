/*Fazer um programa que lê um conjunto de 10 valores e os imprime ordenados.*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int compare( const void* a, const void* b);

int main(void)
{
    int numeros[10];
    printf("Digite 10 valores:\n");
    for (int i = 0; i < 10; i++)
    {
        printf("Valor %i: ", i + 1);
        scanf("%i", &numeros[i]);
    }

    qsort(numeros, 10, sizeof(int), compare );
    
    for (int i = 0; i < 10; i++)
    {
        printf("%i\n", numeros[i]);
    }

    return 0;
}
int compare( const void* a, const void* b)
{
    int int_a = * ( (int*) a );
    int int_b = * ( (int*) b ); 

    return (int_a > int_b) - (int_a < int_b);
}