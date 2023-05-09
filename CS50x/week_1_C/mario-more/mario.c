#include <cs50.h>
#include <stdio.h>

// init constant
#define MAX_HIGH 8

// init variable
int line;
int row;
int space;

// create functions
void create_pyramide(int high);
int high_pyramide(void);

// main logic
int main(void)
{
    //get and check high

    int high = high_pyramide();

    // call function for print pyramids
    create_pyramide(high);
}


// funcion for user input and check valid
int high_pyramide(void)
{
    // get from user high for pyramide
    int high;
    while (true)
    {
        high = get_int("Enter high pyramide: ");

        if (high > 0 && high <= MAX_HIGH)
        {
            break;
        }
    }

    return high;
}

// function for create two pyramide
void create_pyramide(int high)
{
    // cycle for lines
    for (line = 1; line <= high; line++)
    {
        // cycle for space 1
        for (space = high - line; space > 0; space--)
        {
            printf(" ");
        }
        // fold cycle for hash
        for (row = 1; row <= line; row++)
        {
            printf("#");
        }

        printf("  ");

        // fold cycle for hash
        for (row = 1; row <= line; row++)
        {
            printf("#");
        }

        printf("\n");

    }
}
