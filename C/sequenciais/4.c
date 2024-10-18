#include <stdio.h>

double converterTemperatura(double fahrenheit);
int convertTemperature(int fahrenheit);

int main(void)
{
    double fahrenheit;
    int fahrenheit2;
    printf("Digite uma temperatura em Fahrenheit: ");
    scanf("%i", &fahrenheit2);
    int celsius = convertTemperature(fahrenheit2);
    printf("Temperatura em Celsius: %i\n", celsius);
    return 0;
}

double converterTemperatura(double fahrenheit)
{
    double celsius = (fahrenheit - 32.0) * (5.0 / 9.0);
    return celsius;
}
int convertTemperature(int fahrenheit)
{
    int celsius = (fahrenheit - 32) * (5 / 9);
    return celsius;
}