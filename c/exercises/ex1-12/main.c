/* Write a program that prints its input one word per line */

#define IN  1 /* inside a word */
#define OUT 0 /* outside a word */

#include <stdio.h>


main() {

    int state,c;

   
    while((c = getchar()) != EOF){

        if (c == ' ' || c == '\n' || c == '\t'){
            state = OUT; 

        }
            
        else if (state == OUT){
            state = IN;
            printf("\n");
        }
        if (state == IN)
            putchar(c);
    }

}
