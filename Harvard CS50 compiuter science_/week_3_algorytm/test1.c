#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int numbers[] = {4, 6, 8 ,2, 7, 5, 0}; 
    
    //linear search
    for (int i = 0; i < 7; i++)
        if (numbers[i] == 0)
        {
            printf("i found \n");
            return 0;
        } 
    printf("not found \n");
    return 1;

}