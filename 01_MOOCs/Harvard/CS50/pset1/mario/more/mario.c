#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int num;
    int hash;
    int space;
    //Prompt user until valid number between 1 and 23 is provided
    do
    {
        num = get_int("Number: ");
    }
    while (num < 0 || num > 23);

    for (int i = 0; i < num; i++)
    {
        space = num - 1 - i;
        hash = 1 + i;

        for (int j = 0; j < space; j++)
        {
            printf(" ");
        }
        for (int k = 0; k < hash; k++)
        {
            printf("#");
        }
        printf("  ");
        for (int l = 0; l < hash; l++)
        {
            printf("#");
        }
        printf("\n");
    }
}