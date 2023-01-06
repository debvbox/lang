#include <stdio.h>
/*
main ()
{
    long nc;

    nc = 0;
    while(getchar() != EOF)
        ++nc;
    printf("%1d\n",nc);

}
*/

/* second way */
main(){
    double nc;

    for (nc = 0; getchar() != EOF; ++nc)
        ;
    printf("%.0f\n",nc);
}
