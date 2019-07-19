#include<stdio.h>
#include<math.h>
long long unsigned int  prime_factors(long long unsigned int);
int main(){
	printf("%lld\n",log(0xFFFFFFFFFFFFFFFF));
	// printf("%lld\n",prime_factors(0xFFFFFFFFFFFFFFFF));

}
long long unsigned int prime_factors(long long unsigned int n){
	
	for(long long unsigned int j=2;j<n;j++)
	{

long long unsigned int res = (long long unsigned int) pow(pow((log(n)/log(2)),(log(log(n)/log(2)))/log(2)),2);
	for(long long unsigned int i=2;i<=res;i++){
		if(i%res==0) return i;
	}
}
	return 0;
}