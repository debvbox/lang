#include <stdio.h>

/* Print fahrenheit-Celsius Table
 for fahr = 0,20, .... , 300 */
/*
main ()
{
		int fahr, celsius;
		int lower,upper,step;

		lower = 0;   //lower limit of temperature table
		upper = 300; //higher limit of temperature table
		step = 20;   //step size

		fahr = lower;
		while(fahr <= upper)
		{
				celsius = 5 * (fahr - 32) / 9;
				printf("%3d %6d\n",fahr,celsius);
				fahr = fahr + step;
        }
}
*/

//float version
main ()
{
		float fahr, celsius;
		int lower,upper,step;

		lower = 0;   //lower limit of temperature table
		upper = 300; //higher limit of temperature table
		step = 20;   //step size

		fahr = lower;
		while(fahr <= upper)
		{
				celsius = (5.0/9.0)*(fahr-32.0);
                printf("%3.0f %6.1f\n",fahr,celsius);
				fahr = fahr + step;
        }
}
