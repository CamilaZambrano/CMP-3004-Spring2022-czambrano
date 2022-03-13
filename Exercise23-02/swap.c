#include <stdio.h>

void swap(int *d1p, int *d2p){
    int temp0 = *d1p;
    int temp1 = *d2p;
    *d1p = temp1;
    *d2p = temp0;
}
