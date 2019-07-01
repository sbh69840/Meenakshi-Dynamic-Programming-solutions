#include<stdio.h>
#include<stdlib.h>
int main(){
	int n=5;
	int* arr = (int*)calloc(5,sizeof(int));
	for(int i=0;i<5;i++){
		*(arr+i)=i;
	}
	int d;
	scanf("%d",&d);
	int temp;
	for(int i=0;i<d;i++){
		temp = *(arr);
		for(int j=0;j<n-1;j++){

			*(arr+j) = *(arr+j+1);

		}
		*(arr+n-1) = temp;

	}
	printf("[ ");
	for(int i=0;i<n;i++){
		printf("%d ",*(arr+i));
	}
	printf("]");
	return 0;
}
