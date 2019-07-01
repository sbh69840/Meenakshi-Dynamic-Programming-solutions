#include<stdio.h>
int main(){
	
	return 0;
}

int recursion(int x,int y,int w,int z){
	int ways = 0;
	if(x==w && y==z){
		return ways;
	}
	if(x<0 || y<0){
		return 0;
	}
	
}