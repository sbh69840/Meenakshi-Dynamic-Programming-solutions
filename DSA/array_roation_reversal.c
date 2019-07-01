#include<stdio.h>
#include<stdlib.h>
void reverse(int*,int,int);
void rotation(int*,int,int);
int main(){
	int* arr = (int*)calloc(5,sizeof(int));
	for(int i=0;i<5;i++){
		*(arr+i)=i;
	}
	rotation(arr,2,5);
	printf("[ ");
	for(int i=0;i<5;i++){
		printf("%d ",*(arr+i));
	}
	printf("]\n");
	return 0;
}
void reverse(int *arr,int l,int r){
	int i,new_r;
	new_r = (int) (r-l)/2;
	new_r = l+new_r;
	for(i=l;i<new_r;i++){
		*(arr+i)=*(arr+i)^*(arr+r-1-i+l);
		*(arr+r-1-i+l)=*(arr+i)^*(arr+r-1-i+l);
		*(arr+i)=*(arr+i)^*(arr+r-1-i+l);

	}
}
void rotation(int *arr,int d,int n){
	reverse(arr,0,d);
	reverse(arr,d,n);
	reverse(arr,0,n);
}