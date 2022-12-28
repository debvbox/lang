#include <stdio.h>

typedef struct{

    char *name;
    
    int age;
    
}person;

int main(){

    person meme;
    
    meme.name = "Manu";
    
    meme.age = 21;
    
	printf("%s is %d year old\n",meme.name,meme.age);
	
    return 0;
}
    
