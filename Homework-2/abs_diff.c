#include <stdio.h>
#include<stdlib.h>

int abs_diff(int a, int b){
    int diff = a - b;
    if(diff < 0)
        diff = abs(diff);
    return diff;
}