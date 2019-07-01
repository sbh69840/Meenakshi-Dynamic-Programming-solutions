#include<stdio.h>
#include<stdbool.h>
bool recursion(int coins[],int,int);
bool dp(int*,int,int);
int main(){
	
	int coins[]={15,6,3,4,2,1};
	int n = (int)sizeof(coins)/sizeof(int);
	printf("Number of elements in array = %d\n",n);
	int v = 11;
	bool recur = recursion(coins,n,v);
	bool d = dp(coins,n,v);
	printf("%d\n",recur);
	if(d){
		printf("There exists a subset with given sum");
	}else{
		printf("There exists no subset with given sum");
	}
	return 0;
}

bool recursion(int coins[],int n,int v){
	if(v==0){
		return true;
	}
	if(n==0){
		return false;
	}
	if(coins[0]>v){
		return recursion(coins+1,n-1,v);
	}
	return recursion(coins+1,n-1,v)||recursion(coins+1,n-1,v-coins[0]);
}


bool dp(int* coins,int n,int v){
	bool arr[n+1][v+1];
	int i,j;
	for(i=0;i<n+1;i++){
		arr[i][0] = true;
	}
	for(i=1;i<v+1;i++){
		arr[0][i]=false;
	}
	for(i=1;i<n+1;i++){
		for(j=1;j<v+1;j++){
			arr[i][j] = arr[i-1][j]||arr[i-1][j-coins[i-1]];

		}
	}
	return arr[n][v];
}
