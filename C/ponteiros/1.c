/*Procure determinar quais valores são impressos ao final deste programa.
Confira sua resposta testando o programa no micro. Execute-o passo a passo
conferindo o valor das variáveis em cada momento.*/

#include <stdio.h>

void main1();
void main2();
void main3();
void main4();
int calcula(int x);

int main(void)
{
    main1();
    main2();
    main3();
    main4();
    return 0;
}
void main1()
{
    int a, b, *c;

    a = 3;
    b = 4;
    c = &a;
    b++;
    *c = a+2;
    printf("%d %d\n", a, b);
}
void main2()
{
    int a, b, *c;

    a = 4;
    b = 3;
    c = &a;
    *c = *c + 1;
    c = &b;
    b = b+4;
    printf("%d %d %d\n", a, b, *c);
}
void main3()
{
    int a, b, *c, *d, *f;

    a = 4;
    b = 3;
    c = &a;
    d = &b;
    *c /= 2;
    f = c;
    c = d;
    d = f;
    printf("%d %d\n", *c, *d);
}
int calcula(int x)
{
    int i;

    if ((x = x *2) > 5) return (x + 3);
    for (i = 0; i < 10; i++)
    {
        if (i < 5) continue;
        if (x > 8) break;
        x += 2;
    } 
    return (x);
}
void main4()
{
    int a, b, c;
    char d;
    a = 1;
    b = 2;
    c = 3;
    d = 'A';
    a += b * c;
    d = (a > 7) ? d - 1 : d + 1;
    b = calcula(b);
    c = calcula(calcula(a));
    a = c++;
    printf("%d - %d - %d - %c\n", a, b, c, d);
}
