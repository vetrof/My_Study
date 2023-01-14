#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

int letters_count(string text);
int words_count(string text);
int sentient_count(string text);

int main(void) 
{
    string text = get_string("Text: ");
    int letters = letters_count(text);
    int words = words_count(text);
    int sentiens = sentient_count(text);

    float letters_mid = ((float) letters / words) * 100;
    float sentiens_mid = ((float) sentiens / words) * 100;

    float index = 0.0588 * letters_mid - 0.296 * sentiens_mid - 15.8;

    if (index < 1)
    {
        printf("Before Grade 1\n");
    }

    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }

    else
    {
        printf("Grade %i\n", (int) round(index));
    }
    
}

int letters_count(string text)
{    
    int letter_count = 0;
    char c = 0;

    for (int i = 0; i < strlen(text); i++)
    {
        c = text[i];
        if ((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z'))
        {
            letter_count = letter_count + 1;
        }

    }

    return letter_count;
}

int words_count(string text)
{
    int counter = 0;
    char c = 0;

    for (int i = 0; i < strlen(text); i++)		
    {
        c = text[i];
        if ((c == ' ') || (c == '.') || (c == '!') || (c == ','))
        {
            counter = counter + 1;
            if (text[i + 1] == ' ')
            {
                i = i + 1;
            }
        }
        
    }

    return counter;
}

int sentient_count(string text)
{
    int counter = 0;
    char c = 0;

    for (int i = 0; i < strlen(text); i++)		
    {
        c = text[i];
        if ((c == '.') || (c == '!') || (c == '?'))
        {
            counter = counter + 1;
        }
    }
    return counter;
}

