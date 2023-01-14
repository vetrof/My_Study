#include <cs50.h>
#include <stdio.h>

int main(void)
{   
    int cents = 100;
    int quarters = 25;
    int n_quarters = cents / quarters;
    printf("%i\n", n_quarters);
}