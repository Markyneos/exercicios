#include <stdio.h>

int main(void)
{
    for (int i = 1; i <= 9; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            printf("%i x %i = %i\n", i, j + 1, i * (j + 1));
        }
    }
    return 0;
}