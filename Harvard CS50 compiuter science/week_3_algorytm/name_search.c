#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string names[] = {"Bill", "Charlie", "Fred" , "George", "Ginny", "Persie", "Ron"}; 
    
    //linear search
    for (int i = 0; i < 7; i++)
        if (strcmp(names[i], "Ron") == 0)
        {
            printf("i found \n");
            return 0;
        } 
    printf("not found \n");
    return 1;

}