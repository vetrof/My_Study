#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int validator(int n_arg, string argument_input);
void crypto(int key, string text);

int main(int argc, string argv[])
{
    // call validation func
    int flagg = validator(argc, argv[1]);

    // if No valid (flagg = 1) return 1
    if (flagg == 1)
    {
        printf("Usage: ./caesar k\n");
        return 1;
    }

    //if all done to run program
    int key_shift = atoi(argv[1]);
    string phrase = get_string("plaintext:  ");
    crypto(key_shift, phrase);
}

int validator(int n_arg, string argument_input)
{
    // printf("num arg = %i\n", n_arg);
    // printf("arg = %s\n", argument_input);

    // if input two arguments, make other check
    if (n_arg == 2) 
    {
        // test argv[1] to is digit, if not - exit code 1
        for (int i = 0; i < strlen(argument_input); i++)
        {
            char ch = argument_input[i];

            if (isdigit(argument_input[i]))
            {
                // if isdigit no change
            }

            else
            {
                //if is NO digit return 1
                return 1;
            }
        }

    }

    else
    {
        // if no two argument
        return 1;
    }
    return 0;
}

// func for crypto phrase
void crypto(int key, string text)
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
    // return 0;
}
