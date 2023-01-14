#include <cs50.h>
#include <stdio.h>
#include <string.h>

void draw(int high);

int main(void)
{
    int high = 4;
    draw(high);
}

void draw(int n)
{

    if (n <= 0)
    {
        return;
    }

    draw (n - 1);

    for (int i = 0; i < n; i++)
    {
        printf("#");
    }
    printf("\n");
}