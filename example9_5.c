#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#define MAX(a,b) a>b?a:b

int recur(char*,char*,int,int);
int main(){
	int n,m;
	char* str1 = (char*)calloc(100,sizeof(char));
	char* str2 = (char*)calloc(100,sizeof(char));
	scanf("%s",str1);
	scanf("%s",str2);
	n = strlen(str1);
	m = strlen(str2);
	printf("%d %d \n",n,m);
	printf("Recursion result  = %d\n",recur(str1,str2,n,m));
	return 0;
}
int recur(char* str1,char* str2,int n,int m){
	int table[n+1][m+1];
	int i,j;
	for(i=0;i<n+1;i++)
		for(j=0;j<m+1;j++)
			table[i][j]=-1;
	auto int recursion(char*,char*,int,int);
	int recursion(char* str1,char* str2,int n,int m){
		if(table[n][m]!=-1)
			return table[n][m];
		if(n==0 || m==0){
			table[n][m]=0;
			return table[n][m];
		}
		if(str1[n-1]==str2[m-1]){
			table[n][m]=recursion(str1,str2,n-1,m-1)+1;
			return table[n][m];
		}

		table[n][m] = MAX(recursion(str1,str2,n-1,m),recursion(str1,str2,n,m-1));
		return table[n][m];

	}
	return recursion(str1,str2,n,m);
}