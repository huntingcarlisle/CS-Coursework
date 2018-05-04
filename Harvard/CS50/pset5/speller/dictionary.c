// Implements a dictionary's functionality

#include <stdbool.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

node *hashTable[65536];

int sizeDict = 0;

// Hash function
int hashFn(const char *str)
{
    unsigned int hash = 0;
    for (int i = 0, n = strlen(str); i < n; i++)
    {
        hash = (hash << 2) ^ str[i];
    }
    return hash % 65536;
}

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    int wordLength = strlen(word);
    char wordCopy[wordLength + 1];

    for (int i = 0; i < wordLength; i++)
    {
        wordCopy[i] = tolower(word[i]);
    }

    wordCopy[wordLength] = '\0';


    int hashCheck = hashFn(wordCopy);
    node *cursor = hashTable[hashCheck];
    while (cursor != NULL)
    {
        if (strcasecmp(cursor->word, word) == 0)
        {
            return true;
        }
        else
        {
            cursor = cursor->next;
        }
    }
    return false;


}

// Loads dictionary into memory, returning true if successful else
bool load(const char *dictionary)
{

    for (int i = 0; i < 65536; i++)
    {
        hashTable[i] = NULL;
    }

    FILE *dict = fopen(dictionary, "r");
    if (dict == NULL)
    {
        return false;
    }

    while (true)
    {
        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            return false;
        }


        fscanf(dict, "%s", new_node->word);
        new_node->next = NULL;

        if (feof(dict))
        {

            free(new_node);
            break;
        }

        sizeDict++;


        int hashTemp = hashFn(new_node->word);
        node *head = hashTable[hashTemp];

        // if bucket is empty, insert the first node
        if (head == NULL)
        {
            hashTable[hashTemp] = new_node;
        }
        // if bucket is not empty, attach node to front of list
        // design choice: unsorted linked list to minimize load time rather
        // than sorted linked list to minimize check time
        else
        {
            new_node->next = hashTable[hashTemp];
            hashTable[hashTemp] = new_node;
        }
    }


    fclose(dict);
    return true;

}







// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    return sizeDict;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    for (int i = 0; i < 65536; i++)
    {
        node *cursorUnload = hashTable[i];
        while (cursorUnload != NULL)
        {
            node *temp = cursorUnload;
            cursorUnload = cursorUnload->next;
            free(temp);

        }

    }
    return true;

}