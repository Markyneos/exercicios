/*Escrever um programa em "C" que solicita as notas das duas provas feitas por
cada um dos alunos de uma turma (as notas tem de estar no intervalo [0 10]) e
imprime para cada um a média das notas. O programa deve parar
imediatamente após ter sido digitado o valor 50 para a nota da primeira prova.*/

#include <stdio.h>

int main(void)
{
    int quantidade = 0;
    printf("Quantos alunos você deseja inserir a nota: ");
    scanf("%i", &quantidade);

    float nota1[quantidade];
    float nota2[quantidade];
    float medias[quantidade];
    for (int i = 0; i < quantidade; i++)
    {
        do
        {
            printf("Digite a primeira nota do aluno %i: ", i + 1);
            scanf("%f", &nota1[i]);
            if (nota1[i] == 50)
            {
                return 1;
            }
            printf("Digite a segunda nota do aluno %i: ", i + 1);
            scanf("%f", &nota2[i]);
        } while ((nota1[i] < 0 || nota1[i] > 10) || (nota2[i] < 0 || nota2[i] > 10));
        medias[i] = (nota1[i] + nota2[i]) / 2;
    }
    for (int i = 0; i < quantidade; i++)
    {
        printf("A média do aluno %i é: %.2f\n", i + 1, medias[i]);
    }
    return 0;
}