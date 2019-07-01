#include<stdio.h>
#define MAXN 100000
const int primes[] = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71};
int unique_p(int);
int product(int arr[],int);
int sum(int arr[],int);
int solve(int arr[],int,int,int);
struct array{
	int arr[MAXN];
	int k;
};
int main(){
	int n,k,s;
	int arr[n];
	scanf("%d",&n);
	scanf("%d",&k);
	scanf("%d",&s);

	for(int i=0;i<n;i++){
		scanf("%d",&arr[i]);
	}

	printf("%d",solve(arr,n,k,s));
	return 0;
}
int unique_p(int num){
	int res = 0,i;

	for(i=0;i<21;i++){
		if(num%primes[i]==0){
			res+=1;
		}
		while(num%primes[i]==0){
			num = num/primes[i];
		}
	}
	return res;
}
int product(int arr[],int n){
	int i;
	int res=1;
	for(i=0;i<n;i++){
		res*=arr[i];
	}
	return res;
}
int sum(int arr[],int n){
	int i;
	int res = 0;
	for(i=0;i<n;i++){
		res+=arr[i];
	}
	return res;
}

int solve(int arr[],int n,int k,int s){
	int i,j,k_;
	int max_res=0;
	for(i=0;i<n;i++){
		for(j=i+1;j<n;j++){
			struct array sub;
			int sub_sum,sub_prod,n,p,res;
			n = j-i;
			for(k_=i;k_<(j-i);k_++){
				sub.arr[sub.k++]=arr[k_];
			}
			sub_sum = sum(sub.arr,n);

			sub_prod = product(sub.arr,n);

			p = unique_p(sub_prod);
			printf("%d %d\n",sub_sum,sub_prod);
			res = sub_sum*(k-(p*s));

			if(res>max_res){
				max_res=res;
			}
			
		}
	}
	return max_res;

}