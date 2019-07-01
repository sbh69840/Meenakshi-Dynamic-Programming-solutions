#include<stdio.h>
#include<math.h>
#define MAX_WEIGHTS 1000
int input(int*);
int solve(int,int solution[]);
int output(int,int solution[]);
int main(){
	int n,count;
	int solution[MAX_WEIGHTS];
	input(&n);
	count = solve(n,solution);
	output(count,solution);
	return 0;
}
int input(int* n){
	scanf("%d",n);
}
int solve(int n,int solution[]){
	int max_pow_3,sum_series,extra,i;
	max_pow_3 = floor(log10(n)/log10(3));
	sum_series = (pow(3,max_pow_3+1)-1)/2;
	extra = (n-sum_series)<=0?0:(n-sum_series);
	for(i=0;i<(max_pow_3+1);i++){
		solution[i]=pow(3,i);
	}
	if(extra!=0){
		solution[max_pow_3+1]=extra;
		return max_pow_3+2;
	}
	return max_pow_3+1;
}
int output(int count,int solution[]){
	int i;
	printf("The minimum number of weights = %d\n",count);
	printf("The weights are :\n");
	printf("[ ");
	for(i=0;i<count;i++){
		printf("%d ",solution[i]);
	}
	printf("]");
}