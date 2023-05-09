#include <cs50.h>
#include <stdio.h>

//вызываем создание функции которая находится в низу кода
void meow(int n);

int main(void)
{
    meow(11);
}



//функция
void meow(int n)
{
    for (int i = 1; i <= n; i++)
    {
       printf("meow meow meow loop for\n"); 
    }
    
}