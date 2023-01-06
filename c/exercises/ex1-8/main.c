#include <stdio.h>
/* Write a program to count blanks, tabs, and newlines*/

main (){
    int c,newlines,blanks,tabs;

    newlines = 0;
    blanks = 0;
    tabs = 0;

    while((c = getchar()) != EOF){
        if(c == '\n')
            ++newlines;
        if(c == ' ')
            ++blanks;
        if(c == '\t')
            ++tabs;
    }
    printf("\nNew lines: %d\nBlanks: %d\nTabs: %d\n",newlines,blanks,tabs);
}

