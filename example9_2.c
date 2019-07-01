#include <stdio.h>

int recursion1(int,int);
int recursion(int,int,int);
int memo(int,int,int);

int main(){
	int n;
	printf("%s\n","Enter the size of square matrix");
	scanf("%d",&n);
	printf("Recursion1 result = %d\n",recursion1(n-1,n-1));
	printf("Recursion result = %d\n",recursion(0,0,n));
	printf("Memo result = %d\n",memo(0,0,n));
	return 0;
}

int recursion(int x,int y,int n){
	if(x==n-1 || y==n-1){
		return 1;
	}
	if(x==n-1 && y==n-1){
		return 0;
	}
	return recursion(x+1,y,n)+recursion(x,y+1,n);
}
int recursion1(int x,int y){
	if(x==0 || y==0){
		return 1;
	}
	if(x==0 && y==0){
		return 0;
	}
	return recursion1(x-1,y)+recursion1(x,y-1);
}
int memo(int x,int y,int n){
	int memory[n][n];
	int i,j;
	for(i=0;i<n;i++){
		for(j=0;j<n;j++){
			memory[i][j]=0;
		}
	}
	
	auto int solve(int a,int b);
	int solve(int a,int b){
		if(memory[a][b]!=0){
			return memory[a][b];
		}
		if(a==n-1 || b==n-1){
			memory[a][b]=1;
			return memory[a][b];
		}
		if(a==n-1&&b==n-1){
			memory[a][b]=0;
			return memory[a][b];
		}
		memory[a][b]=solve(a+1,b)+solve(a,b+1);
		return memory[a][b];

	}
	solve(0,0);
	return memory[0][0];
}

