/*Exercício: fazer um programa em "C" que solicita o total gasto pelo cliente de
uma loja, imprime as opções de pagamento, solicita a opção desejada e
imprime o valor total das prestações (se houverem).
 1) Opção: a vista com 10% de desconto
 2) Opção: em duas vezes (preço da etiqueta)
 3) Opção: de 3 até 10 vezes com 3% de juros ao mês (somente para compras
acima de R$ 100,00).
OBS: fazer uma função que imprime as opções solicita a opção desejada e retorna
a opção escolhida. No programa principal, testar a opção escolhida e ativar a
função correspondente (uma função para cada opção).*/

#include <stdio.h>

void pagamento(float gasto);

int main(void)
{
    float gasto = 0.0;
    printf("Digite o total gasto: ");
    scanf("%f", &gasto);
    pagamento(gasto);
    return 0;
}
void pagamento(float gasto)
{
    int parcelas = 0;
    int escolha = 0;
    float total = 0.0;
    do
    {
        printf("Selecione uma das opções:\n");
        printf("1) Opção: a vista com 10%% de desconto\n");
        printf("2) Opção: em duas vezes (preço da etiqueta)\n");
        printf("3) Opção: de 3 até 10 vezes com 3%% de juros ao mês (somente para compras acima de R$100.00)\n");
        printf("Escolha: ");
        scanf("%i", &escolha);
        if (escolha == 3 && gasto < 100.0)
        {
            printf("Só é possível realizar essa opção se o valor gasto for maior que R$100.00!\n");
            break;
        }
        switch (escolha)
        {
            case 1:
                total = gasto - (gasto * 0.10);
                printf("O pagamento será de R$%.2f à vista\n", total);
                break;
            case 2:
                total = gasto / 2;
                printf("O pagamento será de %.2f ao mês (2 meses)\n", total);
                break;
            case 3:
                printf("Escolha quantas vezes deseja parcelar (3 a 10): ");
                scanf("%i", &parcelas);
                total = gasto / parcelas;
                total += total * 0.03;
                printf("O pagamento será de R$%.2f em %i parcelas\n", total, parcelas);
                break;
        }
    }
    while (total == 0.0);   
}
