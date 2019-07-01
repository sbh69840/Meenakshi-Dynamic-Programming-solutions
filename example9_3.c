#include<stdio.h>
#include<string.h>
#include <stdbool.h>
#define N 100
int stringinter(char*,char*,char*);
bool dp(char*,char*,char*);
int main(){
	char str1[N];
	char str2[N];
	char str3[N];
	printf("Enter the three srings to check for interleaving \n");
	scanf(" %s %s %s",str1,str2,str3);
	if(stringinter(str1,str2,str3)==1){
		printf("Yes\n");
	}else{
		printf("No\n");
	}
	if(dp(str1,str2,str3)==true){
		printf("Dp solution = Yes\n");
	}else{
		printf("Dp solution = No\n");
	}

	return 0;
}

int stringinter(char* str1,char* str2,char* str3){
	if(strlen(str3)!=(strlen(str1)+strlen(str2))){
		return false;
	}
	if(*str1=='\0' && *str2=='\0' && *str3=='\0'){
		return true;
	}
	int first=false;
	int second = false;
	if(*str1==*str3){
		first =  stringinter(str1+1,str2,str3+1);
	}
	if(*str2==*str3){
		second = stringinter(str1,str2+1,str3+1);
	}
	return (first||second);
}
bool dp(char* str1,char* str2,char* str3){
	int a = strlen(str1);
	int b = strlen(str2);
	bool memo[a+1][b+1];
	int i,j;
	memo[0][0]=true;
	for(i=1;i<=a;i++){
		if(str1[i-1]!=str3[i-1]){
			memo[i][0]=false;
		}else{
			memo[i][0]=memo[i-1][0];
		}
	}
	for(i=1;i<=b;i++){
		if(str2[i-1]!=str3[i-1]){
			memo[0][i]=false;
		}else{
			memo[0][i]=memo[0][i-1];
		}
	}
	for(i=1;i<=a;i++){
		for(j=1;j<=b;j++){
			if(str1[i-1]==str2[j-1] && str1[i-1]==str3[i+j-1]){
				memo[i][j]=(memo[i][j-1]||memo[i-1][j]);
			}
			else if(str1[i-1]==str3[i+j-1]){
				memo[i][j] = memo[i-1][j];
			}
			else if(str2[j-1]==str3[i+j-1]){
				memo[i][j]=(memo[i][j-1]);
			}
			else{
				memo[i][j]=false;
			}


		}
	}
	for(i=0;i<=a;i++){
		for(j=0;j<=b;j++){
			printf("%d ",memo[i][j]);
		}
		printf("\n");
	}
	return memo[a][b];
}
