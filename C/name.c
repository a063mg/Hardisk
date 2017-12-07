#include <stdio.h>

int main(void)
{
char name[32];
char prename[32];
FILE * newfile;
newfile = fopen("names.csv", "r");
printf("%s", newfile);
fclose(newfile);
printf("Enter your name: \n");
scanf("%s", name); 
printf("Enter your prename: \n");
scanf("%s", prename); 
FILE * file;
file = fopen("names.csv", "w+");
fprintf(file, "%s,%s\n", name, prename);
fclose(file); 
}

