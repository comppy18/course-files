#include <stdio.h>          
main() {                    
FILE *fp;                   
double pi = 3.1415927;      
fp=fopen("cfile","wb");     
fwrite(&pi,sizeof(pi),1,fp);
fclose(fp);                 
}                           

