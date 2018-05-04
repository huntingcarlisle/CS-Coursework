#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        string plain = get_string("plaintext: ");
        string cipher = plain;
        printf("ciphertext: ");
        int k = atoi(argv[1]);
        k = k % 26;

        for (int i = 0, n = strlen(plain); i < n; i++)
        {
            if (plain[i] > 64 && plain[i] < 91)
            {
                cipher[i] = plain[i] + k;
                if (cipher[i] > 90)
                {
                    cipher[i] -= 26;
                }
                printf("%c", cipher[i]);
            }
            else if (plain[i] > 96 && plain[i] < 123)
            {
                cipher[i] = -32 + plain[i] + k;
                if (cipher[i] > 90)
                {
                    cipher[i] -= 26;
                }
                printf("%c", cipher[i] + 32);
            }
            else
            {
                printf("%c", plain[i]);
            }
        }
        printf("\n");
    }
    else
    {
        printf("Usage: ./caesar k\n");
        return 1;
    }
}