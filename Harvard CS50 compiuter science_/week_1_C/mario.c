#include <cs50.h>
#include <stdio.h>

int main(void)
{
	int n;
	while(true)
	{
		n = get_int("n: ");
		if (n > 0)
		{
			break;
		}
	}


	printf("%i\n", n);

}