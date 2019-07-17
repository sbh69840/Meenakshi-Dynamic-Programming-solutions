#include<stdio.h>
int main(){
	int x,y,shift;
	shift=2;
	x = 2;
	y = (x << shift) | (x >> (sizeof(x)*8 - shift));
	printf("%d %d %d",y,(x << shift),(x >> (sizeof(x)*8 - shift)));
	return 0;
}