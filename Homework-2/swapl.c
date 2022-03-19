#include <stdio.h>

void swapl(long *d1p, long *d2p){
    long temp0 = *d1p;
    long temp1 = *d2p;
    *d1p = temp1;
    *d2p = temp0;
}
