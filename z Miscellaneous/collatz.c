#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int collatz(int n);
int l;

int main(void)
{

    do
    {
        l = get_int("Positive integer: ");

    }
    while (l < 1);
    int answer = collatz(l);
    printf("%i\n", answer);
}
int collBase;
int coll = 0;

//Return the sum of 1 through m
int collatz(int n)
{
    for (int i = 0; i < l; i++)
    {
        collBase = i;
        if (n==1)
        {
            return 0;
        }
        else
        {
            if (n % 2 == 0)
            {
                n = collatz(n/2);
                coll++;

            }
            else
            {
                n = collatz(3* n + 1);
                coll++;
            }
        }
        printf("%i\n", collBase);
        return coll;
    }
    return coll;
}