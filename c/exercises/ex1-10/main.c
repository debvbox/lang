#include <stdio.h>
/*Exercise 1.10 page 20 The C programming book*/
main () {

    int c;

    while((c = getchar()) != EOF){
        if(c == '\t')
            printf("/ t");
    }


}

