#include <stdio.h>
#include <cs50.h>
#include <math.h>
#include <string.h>

int main(void)
{
    long long cc;

    long long x = 10;
    int length = 0;
    long long ccSub = 0;
    do
    {
        cc = get_long_long("Number: ");
    }
    while (cc < 0);
    long long ccTwo = cc;
    do
    {
        ccTwo = ccTwo / 10;
        length++;
    }
    while (ccTwo > 0);
    // printf("%d",length);
    // printf("\n");
    // printf("%llu",cc);
    // printf("\n");
    // printf("%llu",ccTwo);
    // printf("\n");

    // printf("%lu",strlen(cc));
    for (int i = 0; i < length; i++)
    {
        int ccMod = ((cc % (x * 10)) / x);
        if (ccMod > 4)
        {
        printf("WIP");
        }
        else
        {
            ccSub += ccMod;
        }
        x = x * 100;
    }
    printf("%lld",ccSub);
    printf("\n");
}