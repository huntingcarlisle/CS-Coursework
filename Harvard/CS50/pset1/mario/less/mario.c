#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int num;
    int hash;
    int space;
    do
    {
        num = get_int("Number: ");
    }
    while (num < 0 || num > 23);

    for (int i = 0; i < num; i++)
    {
        space = num - 1 - i;
        hash = 2 + i;

        for (int j = 0; j < space; j++)
        {
            printf(" ");
        }
        for (int k = 0; k < hash; k++)
        {
            printf("#");
        }
        printf("\n");
    }
}