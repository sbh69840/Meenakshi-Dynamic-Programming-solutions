#include<stdio.h>
#define MAX(a,b) a>b?a:b

int recursion(int arr[],int,int sub[],int,int);
int main(){
	int arr[] = {1,6,2,5,3,4,5};
	int len_arr = 7;
	int subarr[6];
	printf("%d\n",recursion(arr,0,subarr,0,len_arr));
	return 0;
}


int recursion(int arr[],int index,int subarr[],int sub_len,int len_arr){
	int first,second;
	if(index==len_arr){
		int i;
		printf("[ ");
		for(i=0;i<sub_len;i++){
			printf("%d ",subarr[i]);
		}
		printf(" ]\n");

		return sub_len;
	}else{
		if(sub_len>0){
			if(arr[index]>subarr[sub_len-1]){
				first = recursion(arr,index+1,subarr,sub_len,len_arr);
				subarr[sub_len] = arr[index];
				second = recursion(arr,index+1,subarr,sub_len+1,len_arr);
			}else{
				first = recursion(arr,index+1,subarr,sub_len,len_arr);
				second = 0;
			}
		}else{
			first = recursion(arr,index+1,subarr,sub_len,len_arr);
			subarr[sub_len] = arr[index];
			second = recursion(arr,index+1,subarr,sub_len+1,len_arr);
		}
	}
	return MAX(first,second);
}