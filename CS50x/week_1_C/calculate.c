#include <cs50.h>
#include <stdio.h>

int main(void)

{
	//input number 1
	long x = get_long("x: ");

	//input number 2
	long y = get_long("y: ");

	//print 1 and 2 number
	printf("x = %li\n", x);
	printf("y = %li\n", y);

	//summ and print result number
	printf("summ x and y = %li\n", x + y);
}
