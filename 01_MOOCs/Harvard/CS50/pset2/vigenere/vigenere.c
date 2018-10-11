#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        string k = argv[1];
        int good = 1;
        for (int j = 0; j < strlen(k) && good == 1; j++)
        {
            if (isalpha(k[j]))
            {
                good = 1;
            }
            else
            {
                good = 0;
            }
        }

        if (good == 1)
        {
            string plain = get_string("plaintext: ");
            string cipher = plain;
            printf("ciphertext: ");

            // printf("%s",k);
            // k = k % 26;
            int currK = 0;

            // printf("%i", currK);
            for (int i = 0, j = 0, n = strlen(cipher); i < n; i++)
            {
                if (j >= strlen(k))
                {
                    j = 0;
                }
                currK = k[j];
                if (currK < 91)
                {
                    currK -= 65;
                }
                else
                {
                    currK -= 97;
                }
                if (cipher[i] > 64 && cipher[i] < 91)
                {

                    cipher[i] = cipher[i] + currK;
                    if (cipher[i] > 90)
                    {
                        cipher[i] -= 26;
                    }
                    printf("%c", cipher[i]);
                    j++;
                }
                else if (cipher[i] > 96 && cipher[i] < 123)
                {
                    cipher[i] = -32 + cipher[i] + currK;
                    if (cipher[i] > 90)
                    {
                        cipher[i] -= 26;
                    }
                    printf("%c", cipher[i] + 32);
                    j++;
                }
                else
                {
                    printf("%c", cipher[i]);
                }


            }
        }
        else
        {
            printf("Usage: ./vigenere k\n");
            return 1;
        }



        printf("\n");
    }
    else
    {
        printf("Usage: ./vigenere k\n");
        return 1;
    }
}