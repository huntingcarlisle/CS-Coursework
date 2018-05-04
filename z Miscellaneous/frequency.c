#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>



int frequency(string note)
{

    int numberOfSemitones = 0; //(difference between note and A4)


   //  int notePlayed = (if len == 2, then get char[0]; else get char[0,1]);
   //  int octavePlayed = (if len == 2, then get char[1]; else get char[1,2]);
    int octavePlayed;
    string notePlayed;
    if (strlen(note) == 3) {
      char tempNotePlayed[3] = {note[0], note[1], '\0'};
      notePlayed = tempNotePlayed;
      octavePlayed = note[2] - '0';
    }
    else {
      char tempNotePlayed[2] = {note[0], '\0'};
      notePlayed = tempNotePlayed;
      octavePlayed = note[1] - '0';
    }


    // modify numberOfSemitones based on notePlayed
      if (strcmp(notePlayed, "A") == 0) {
         numberOfSemitones = 0;
         numberOfSemitones = numberOfSemitones + (12 * (octavePlayed - 4));
      }
      else if (strcmp(notePlayed, "Bb") == 0) {
         numberOfSemitones += 1;
         numberOfSemitones = numberOfSemitones + (12 * (octavePlayed - 4));
      }
      else if (strcmp(notePlayed, "A#") == 0) {
         numberOfSemitones += 1;
         numberOfSemitones = numberOfSemitones + (12 * (octavePlayed - 4));
      }
      else if (strcmp(notePlayed, "B") == 0) {
         numberOfSemitones += 2;
         numberOfSemitones = numberOfSemitones + (12 * (octavePlayed - 4));
      }
      else if (strcmp(notePlayed, "C") == 0) {
         numberOfSemitones += 3;
         numberOfSemitones = numberOfSemitones + (12 * (octavePlayed - 5));
      }
      else if (strcmp(notePlayed, "Db") == 0) {
         numberOfSemitones += 4;
         numberOfSemitones = numberOfSemitones + (12 * (octavePlayed - 5));
      }
      else if (strcmp(notePlayed, "C#") == 0) {
         numberOfSemitones += 4;
         numberOfSemitones = numberOfSemitones + (12 * (octavePlayed - 5));
      }
      else if (strcmp(notePlayed, "D") == 0) {
         numberOfSemitones += 5;
         numberOfSemitones = numberOfSemitones + (12 * (octavePlayed - 5));
      }
      else if (strcmp(notePlayed, "Eb") == 0) {
         numberOfSemitones += 6;
         numberOfSemitones = numberOfSemitones + (12 * (octavePlayed - 5));
      }
      else if (strcmp(notePlayed, "D#") == 0) {
         numberOfSemitones += 6;
         numberOfSemitones = numberOfSemitones + (12 * (octavePlayed - 5));
      }
      else if (strcmp(notePlayed, "E") == 0) {
         numberOfSemitones += 7;
         numberOfSemitones = numberOfSemitones + (12 * (octavePlayed - 5));
      }
      else if (strcmp(notePlayed, "F") == 0) {
         numberOfSemitones += 8;
         numberOfSemitones = numberOfSemitones + (12 * (octavePlayed - 5));
      }
      else if (strcmp(notePlayed, "Gb") == 0) {
         numberOfSemitones += 9;
         numberOfSemitones = numberOfSemitones + (12 * (octavePlayed - 5));
      }
      else if (strcmp(notePlayed, "F#") == 0) {
         numberOfSemitones += 9;
         numberOfSemitones = numberOfSemitones + (12 * (octavePlayed - 5));
      }
      else if (strcmp(notePlayed, "G") == 0) {
         numberOfSemitones += 10;
         numberOfSemitones = numberOfSemitones + (12 * (octavePlayed - 5));
      }
      else if (strcmp(notePlayed, "Ab") == 0) {
         numberOfSemitones += 11;
         numberOfSemitones = numberOfSemitones + (12 * (octavePlayed - 5));
      }
      else if (strcmp(notePlayed, "G#") == 0) {
         numberOfSemitones += 11;
         numberOfSemitones = numberOfSemitones + (12 * (octavePlayed - 5));
      }

    double powerRaise = (double)numberOfSemitones / 12;
    int frequencyHertz = (pow(2, powerRaise) * 440);
    printf("%i\n", frequencyHertz);
    return frequencyHertz;
}


int main(void)
{
    string name = get_string("Note: ");
    frequency(name);
}
