#include <cs50.h>
#include <stdio.h>
float discount15(float price, int percent_off);


int main(void)
{
	float regular = get_float("regular price: ");
	int percent_off = get_int("percent off: ");
	float disc = discount15(regular, percent_off);
	printf("new cost = %.2f\n", disc);
}



float discount15(float price, int percent_off)
{

	return price * (100 - percent_off) / 100;

}