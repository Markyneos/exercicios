/*Escrever a seqüência de comandos do pré-processador que define o tipo de
dados BOOL (com as constantes TRUE e FALSE) caso isso ainda não tenha
sido feito.*/

#include <stdio.h>

#ifndef BOOL
    #define BOOL int
    #define TRUE 1
    #define FALSE 0
#endif

BOOL verificar(int resposta);

int main(void)
{
    int resposta;
    printf("Quantas vezes o Brasil foi ganhador da copa do mundo?: ");
    scanf("%i", &resposta);

    if (verificar(resposta) == TRUE)
    {
        printf("Acertou!\n");
    }
    else
    {
        printf("Errou!\n");
    }
    return 0;
}
BOOL verificar(int resposta)
{
    if (resposta == 5)
    {
        return TRUE;
    }
    else
    {
        return FALSE;
    }
}