#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    string name = get_string("Fraction: ");
    char initials[4];
    int counter = 0;
    for (int i = 0; i < strlen(name); i++)
    {
        if (isupper(name[i]))
        {
         initials[counter] = name[i];
         counter++;
        }
    }
    initials[counter] = '\0' ;
    printf("%s\n", initials);
}




#include <cs50.h>
#include <math.h>
#include <stdlib.h>

#include "helpers.h"



// Converts a fraction formatted as X/Y to eighths
int duration(string fraction)
{
    int fractionNumerator = atoi(fraction[0]);
    int fractionDenominator;
    int fractionDenominatorInt;
    if (strlen(fraction) > 3) {
        fractionDenominator = fraction[2];
        for (int i = 3; i < strlen(fraction); i++) {
            fractionDenominator = fractionDenominator + fraction[i];
        }
        fractionDenominatorInt = atoi(fractionDenominator)
    }
    else {
        fractionDenominatorInt = atoi(fraction[2])
    }

    int eighthsNumerator = (8 * x) / y;

    return eightsNumerator;


}