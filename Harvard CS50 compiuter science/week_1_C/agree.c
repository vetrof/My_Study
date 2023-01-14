#include <cs50.h>
#include <stdio.h>

int main(void)
{

	char x = get_char("you agree? y/n ");

	if (x == 'y' || x == 'Y')
	{
		printf("you agree\n");
	}

	else if (x == 'n' || x == 'N')
	{
		printf("you NOT agree\n");
	}
}	
