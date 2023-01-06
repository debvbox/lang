#include <stdio.h>

/* Copy input to output ; 1st version*/
/*
main (){
    int c;

    c = getchar();
    while(c != EOF){
        putchar(c);
        c = getchar();
    }
}
*/
//END OF FILE (EOF) is ctrl + d xddd
//
//2nd version
int main () {
    int c;
    printf("%d\n",EOF);
    while((c=getchar()) != EOF){
        putchar(c);
    }
    return 0;
}
