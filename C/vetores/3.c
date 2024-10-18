/*Fazer uma rotina que recebe como parâmetro um array de 5 posições contendo
as notas de um aluno ao longo do ano e devolve a média do aluno.
*/
#include <stdio.h>

float media(float notas[5]);

int main(void)
{
    float notas[5];

    printf("Digite as notas do aluno:\n");
    for (int i = 0; i < 5; i++)
    {
        printf("Nota %i: ", i + 1);
        scanf("%f", &notas[i]);
    }

    float var_media = media(notas);
    printf("A média do aluno é: %.2f\n", var_media);
    return 0;
}
float media(float notas[5])
{
    float total = 0.0;
    for (int i = 0; i < 5; i++)
    {
        total += notas[i];
    }
    total /= 5;
    return total;
}