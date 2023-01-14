#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int crypto(int key, string text);

int main(int argc, string argv[])
{
    string argument = argv[1];

    // check to two arguments
    if (argc == 2) 
    {
        // test argv[1] to is digit, if not - exit code 1
        for (int i = 0; i < strlen(argument); i++)
        {
            char ch = argument[i];
            if (isdigit(argument[i]))
            {
                // if isdigit no change
            }

            else
            {
                // if char NO digit
                printf("Usage: ./caesar k\n");
                return 1;
            }
        }

        // if all done to run program
        int key_shift = atoi(argv[1]);
        string phrase = get_string("plaintext:  ");
        crypto(key_shift, phrase);
        return 0;

    }

    // if input argument no correct return code 1
    else
    {
        printf("Usage: ./caesar k\n");
        return 1;
    }
}

// func for crypto phrase
int crypto(int key, string text)
{
    char shift_char;
    printf("ciphertext: ");

    // create cycle for phrase
    for (int i = 0; i < strlen(text); i++)
    {
        // if small symbol
        if (text[i] >= 'a' && text[i] <= 'z')
        {   
            // change symbol ascii code
            shift_char = ((text[i] + key) - 96) % 26;
            printf("%c", shift_char + 96);
        }

        // if BIG symbol
        else if (text[i] >= 'A' && text[i] <= 'Z')
        {
            shift_char = ((text[i] + key) - 64) % 26;
            printf("%c", shift_char + 64);
        }

        // if not letters, no change
        else
        {
            printf("%c", text[i]);
        }
    }

    printf("\n");
    return 0;
}
