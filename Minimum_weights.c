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
	int res=0,count=0,i,pow_3;
	while(1){
		pow_3 = pow(3,count);
		res+=pow_3;
		if(pow_3>n){
			res-=pow_3;
			break;
		}
		solution[count]=pow_3;
		count++;
	}
	if((n-res)<=0){
		return count;
	}else{
		solution[count]=(n-res);
	}
	return count+1;
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