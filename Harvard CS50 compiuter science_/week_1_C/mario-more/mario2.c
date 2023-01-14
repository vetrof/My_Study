#include <cs50.h>
#include <stdio.h>

// init variable
int high;
int line;
int row;
int space;
int neg_row;

// constant for amount pyramide
const int N_PY = 2;

// create functions
void create_pyramide(int high);
int high_pyramide(void);

int main(void) 
{
	//get and check high
	high = high_pyramide();

	// call function for print pyramids
	create_pyramide(high);  
}


// ----- function area -----

// function for create two pyramide
void create_pyramide(int high)
{
		// cycle for  line
	for (line = 1; line <= high; line++)
	{	
		// fold cycle for row
		for(row = 1; row <= line; row++)
		{
			printf("#");
		}

		// cycle for space
		for (space = (high * N_PY) - (line * N_PY); space > 0; space-- )
		{
			printf(" ");
		}

		// cycle for negative row
		for (neg_row = 1; neg_row <= line; neg_row++)
		{
			printf("#");
		}

		printf("\n");
	
	}
}


// funcion for user input and check valid 
int high_pyramide(void)
{
	// get from user high for pyramide
	while(true)
	{
		high = get_int("Enter high pyramide: ");

		if (high > 0 && high <=8)
		{
			break;
		}
	}

	return high;
}

	

