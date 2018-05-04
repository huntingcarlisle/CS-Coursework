#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    float change;
    int coins = 0;
    do
    {
        change = get_float("Change owed: ");
    }
    while (change < 0);

    int changeTwo = round(change * 100);
    for (int i = 0; changeTwo >= 25; i++)
    {
        changeTwo = changeTwo - 25;
        coins++;
    }
    for (int j = 0; changeTwo >= 10; j++)
    {
        changeTwo = changeTwo - 10;
        coins++;
    }
    for (int k = 0; changeTwo >= 5; k++)
    {
        changeTwo = changeTwo - 5;
        coins++;
    }
    for (int l = 0; changeTwo > 0; l++)
    {
        changeTwo = changeTwo - 1;
        coins++;
    }


    printf("%d", coins);
    printf("\n");
}