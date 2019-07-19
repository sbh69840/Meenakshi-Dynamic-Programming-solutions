#include<stdio.h>
#include<stdlib.h>
int back_main(int*,int,int);
int main(){
	int n = 6;
	int coins1[] = {1,2,5,10,20,50};
	int* coins = (int*) calloc(n,sizeof(int));
	coins = coins1;
	for(int i=0;i<n;i++){
		printf("%d\n",*(coins+i));
	}
	printf("%d\n",back_main(coins,n,65));
	return 0;
}
int back_main(int* arr,int n,int S){
	int* memo = (int*) calloc(S+1,sizeof(int));
	auto int backtrack(int*,int,int);
	int backtrack(int* arr,int n,int S){
		if(memo[S]!=0){
			return memo[S];
		}
		if(S==0){
			return 0;
		}else{
			int res = INT_MAX;
			for(int i=0;i<n;i++){
				if(*(arr+i)<=S){
					int temp = backtrack(arr,n,S-*(arr+i));
					if((temp+1)<res){
						res = temp+1;
					}
				}
			}
			memo[S]=res;
			return res;
		}
	}
	return backtrack(arr,n,S);
}