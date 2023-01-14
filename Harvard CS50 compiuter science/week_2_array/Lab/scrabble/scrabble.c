#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // winner is
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }

    else if (score1 == score2)
    {
        printf("Tie!\n");
    }

    else
    {
        printf("Player 2 wins!\n");
    }
}

int compute_score(string word)
{
    // init variable
    int score = 0;
    int ascii = 0;
    int diference = 32; // differece ascii uper and lower char
    int point = 0;

    // cycle for one char in word
    for (int i = 0; i < strlen(word); i++)
    {
        // if char is lower, assci code down to ascii upper char
        if (islower(word[i]))
        {
            ascii = word[i] - 32; 
        }

        else 
        {
            ascii = word[i];
        }

        // if char not letter, no add to score = 0
        if (ascii >= 'A' && ascii <= 'Z')
        {
            // get score with ascii code minus 65 (ascii code symbol 'A')
            // and add score to score variable
            score = score + POINTS[ascii - 'A'];
        }

    }

    return score;
}
