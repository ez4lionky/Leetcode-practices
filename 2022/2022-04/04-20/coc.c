#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

int main()
{
    char l[81];
    scanf("%[^\n]", l);

    // Write an answer using printf(). DON'T FORGET THE TRAILING \n
    // To debug: fprintf(stderr, "Debug messages...\n");
    // fprintf(stderr, l);
    int len = strlen(l);
    printf("len: %d\n", len);
    // int i = 81;
    // while(i >= 0){
    //     if l[i]:
    //         continue
    //     int j = i;
    //     while(j<len){
    //         printf(l[j]);
    //         j++;
    //     }
    //     j = 0;
    //     while(j<i){
    //         printf(l[j]);
    //         j++;
    //     }
    //     printf("\n");
    //     i--;
    // }
    return 0;
}
