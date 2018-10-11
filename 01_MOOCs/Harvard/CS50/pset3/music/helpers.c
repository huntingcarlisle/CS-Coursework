// Helper functions for music

#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>



#include "helpers.h"

// Converts a fraction formatted as X/Y to eighths
int duration(string fraction)
{
    int fractionNumerator, fractionDenominator;
    sscanf(fraction, "%d/%d", &fractionNumerator, &fractionDenominator);
    int eighthsNumerator = (8 * fractionNumerator) / fractionDenominator;
    return eighthsNumerator;
}


// Calculates frequency (in Hz) of a note
int frequency(string note)
{

    int numberOfSemitones = 0;
    int octavePlayed;
    char *notePlayed;
    if (strlen(note) == 3)
    {
        char tempNotePlayed[3] = {note[0], note[1], '\0'};
        notePlayed = tempNotePlayed;
        octavePlayed = note[2] - '0';
    }
    else
    {
        char tempNotePlayed[2] = {note[0], '\0'};
        notePlayed = tempNotePlayed;
        octavePlayed = note[1] - '0';
    }


    // modify numberOfSemitones based on notePlayed
    if (strcmp(notePlayed, "A") == 0)
    {
        numberOfSemitones = 0;
        numberOfSemitones = numberOfSemitones + (12 * (octavePlayed - 4));
    }
    else if (strcmp(notePlayed, "Bb") == 0)
    {
        numberOfSemitones += 1;
        numberOfSemitones = numberOfSemitones + (12 * (octavePlayed - 4));
    }
    else if (strcmp(notePlayed, "A#") == 0)
    {
        numberOfSemitones += 1;
        numberOfSemitones = numberOfSemitones + (12 * (octavePlayed - 4));
    }
    else if (strcmp(notePlayed, "B") == 0)
    {
        numberOfSemitones += 2;
        numberOfSemitones = numberOfSemitones + (12 * (octavePlayed - 4));
    }
    else if (strcmp(notePlayed, "C") == 0)
    {
        numberOfSemitones += 3;
        numberOfSemitones = numberOfSemitones + (12 * (octavePlayed - 5));
    }
    else if (strcmp(notePlayed, "Db") == 0)
    {
        numberOfSemitones += 4;
        numberOfSemitones = numberOfSemitones + (12 * (octavePlayed - 5));
    }
    else if (strcmp(notePlayed, "C#") == 0)
    {
        numberOfSemitones += 4;
        numberOfSemitones = numberOfSemitones + (12 * (octavePlayed - 5));
    }
    else if (strcmp(notePlayed, "D") == 0)
    {
        numberOfSemitones += 5;
        numberOfSemitones = numberOfSemitones + (12 * (octavePlayed - 5));
    }
    else if (strcmp(notePlayed, "Eb") == 0)
    {
        numberOfSemitones += 6;
        numberOfSemitones = numberOfSemitones + (12 * (octavePlayed - 5));
    }
    else if (strcmp(notePlayed, "D#") == 0)
    {
        numberOfSemitones += 6;
        numberOfSemitones = numberOfSemitones + (12 * (octavePlayed - 5));
    }
    else if (strcmp(notePlayed, "E") == 0)
    {
        numberOfSemitones += 7;
        numberOfSemitones = numberOfSemitones + (12 * (octavePlayed - 5));
    }
    else if (strcmp(notePlayed, "F") == 0)
    {
        numberOfSemitones += 8;
        numberOfSemitones = numberOfSemitones + (12 * (octavePlayed - 5));
    }
    else if (strcmp(notePlayed, "Gb") == 0)
    {
        numberOfSemitones += 9;
        numberOfSemitones = numberOfSemitones + (12 * (octavePlayed - 5));
    }
    else if (strcmp(notePlayed, "F#") == 0)
    {
        numberOfSemitones += 9;
        numberOfSemitones = numberOfSemitones + (12 * (octavePlayed - 5));
    }
    else if (strcmp(notePlayed, "G") == 0)
    {
        numberOfSemitones += 10;
        numberOfSemitones = numberOfSemitones + (12 * (octavePlayed - 5));
    }
    else if (strcmp(notePlayed, "Ab") == 0)
    {
        numberOfSemitones += 11;
        numberOfSemitones = numberOfSemitones + (12 * (octavePlayed - 5));
    }
    else if (strcmp(notePlayed, "G#") == 0)
    {
        numberOfSemitones += 11;
        numberOfSemitones = numberOfSemitones + (12 * (octavePlayed - 5));
    }

    double powerRaise = (double)numberOfSemitones / 12;
    int frequencyHertz = round((pow(2, powerRaise) * 440));
    return frequencyHertz;
}

// Determines whether a string represents a rest
bool is_rest(string s)
{
    if (s[0] == '\0')
    {
        return true;
    }
    else
    {
        return false;
    }
}
