#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

// Converts a fraction formatted as X/Y to eighths
int duration(string fraction)
{
    int fractionNumerator, fractionDenominator;
    sscanf(fraction, "%d/%d", &fractionNumerator, &fractionDenominator);
    int eighthsNumerator = (8 * fractionNumerator) / fractionDenominator;
    printf("%i\n", eighthsNumerator);
    return eighthsNumerator;
}

int main(void)
{
    string name = get_string("Fraction: ");
    duration(name);
}


