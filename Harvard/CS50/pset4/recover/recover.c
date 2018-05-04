// Copies a BMP file

#include <stdio.h>
#include <stdlib.h>

// #include "jpg.h"

int main(int argc, char *argv[])
{
    // ensure proper usage
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./recover image\n");
        return 1;
    }


    char *imgFile = argv[1];

    // Open Source File
    FILE *imgptr = fopen(imgFile, "r");
    if (imgptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", imgFile);
        return 2;
    }


    // Set Jpeg counter to -1
    int jpgCounter = -1;
    unsigned char inptr[512];
    FILE *jpgptr;
    char filename[8];
    while (fread(inptr, 512, 1, imgptr) == 1)
        if (inptr[0] == 0xff && inptr[1] == 0xd8 && inptr[2] == 0xff && (inptr[3] & 0xf0) == 0xe0)
        {
            jpgCounter++;
            if (jpgCounter >= 1)
            {
                fclose(jpgptr);
            }
            sprintf(filename, "%03i.jpg", jpgCounter);
            jpgptr = fopen(filename, "w");
            fwrite(inptr, 512, 1, jpgptr);
        }
        else
        {
            if (jpgCounter >= 0)
            {
                fwrite(inptr, 512, 1, jpgptr);
            }
            // else
            // {
            //     // seek to beginning of next block
            // }
            //     // return
        }

    fclose(jpgptr);
}
