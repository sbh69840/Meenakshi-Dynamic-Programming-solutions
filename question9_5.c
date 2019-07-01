#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include <stdbool.h>
void swap(char*,char*);
void str_permute(char*,char*,int,int,int);
long fact(int);
bool isInterleaving(char*,char*,char*);
bool isInterleaving_dp(char*,char*,char*);
int main(){
	char* a = (char*) calloc(100,sizeof(char));
	printf("Enter string A\n");
	scanf("%s",a);
	char* b = (char*) calloc(100,sizeof(char));
	printf("Enter string B\n");
	scanf("%s",b);
	char* c = (char*) calloc(200,sizeof(char));
	printf("Joining string 1 and string2\n");
	for(int i=0;i<strlen(a);i++){
		*(c+i) = *(a+i);
	}
	for(int i=0;i<strlen(b);i++){
		*(c+strlen(a)+i) = *(b+i);
	}

	char* final = (char*) calloc(fact(strlen(c))*strlen(c),sizeof(char));
	if(final==NULL){
		printf("Memory not allocated\n");
		exit(0);
	}else{
		printf("Memory allocated\n");
	}
	*(final) = '\0';
	

	str_permute(final,c,0,(strlen(c)-1),strlen(c));
	printf("Printing the permutes interleaving with a and b");
	int i,j;
	for(i=0;i<strlen(final);i+=strlen(c)){
		char* sub = (char*) calloc(strlen(c),sizeof(char));
		for(j=0;j<strlen(c);j++){
			*(sub+j) = *(final+i+j);

		}
		if(isInterleaving_dp(a,b,sub)){
			printf("\n | %s | \n",sub);
		} 

	}
	free(final);
	free(a);
	return 0;
}
bool isInterleaving_dp(char* str1,char* str2,char* str3){
	int a = strlen(str1);
	int b = strlen(str2);

	bool dp[a+1][b+1];
	dp[0][0] = true;

	int i ,j;
	for(i = 1;i<a+1;i++){
		if(str1[i-1]!=str3[i-1]){
			dp[i][0] = false;

		}else{
			dp[i][0] = dp[i-1][0];
		}
	}
	for(i=1;i<b+1;i++){
		if(str2[i-1]!=str3[i-1]){
			dp[0][i] = false;
		}else{
			dp[0][i] = dp[0][i-1];
		}
	}
	for(i=1;i<a+1;i++){
		for(j=1;j<b+1;j++){
			if(str1[i-1]==str2[j-1] && (str1[i-1]==str3[i+j-1])){
				dp[i][j] = dp[i-1][j]||dp[i][j-1];
			}
			else if(str1[i-1]==str3[i+j-1]){
				dp[i][j] = dp[i-1][j];
			}
			else if(str2[j-1]==str3[i+j-1]){
				dp[i][j] = dp[i][j-1];
			}else{
				dp[i][j] = false;
			}
		}
	}
	return dp[a][b];
}
bool isInterleaving(char* str1,char* str2, char* str3){
	if(strlen(str1)==0 && strlen(str2)==0 && strlen(str3)==0){
		return true;
	}
	bool first = false;
	bool second = false;
	if(*str1==*str3){
		first =  isInterleaving(str1+1,str2,str3+1);
	}
	if(*str2==*str3){
		second = isInterleaving(str1,str2+1,str3+1);
	}
	return first||second;


}

void swap(char* a,char* b){
	char tmp;
	tmp = *a;
	*a = *b;
	*b = tmp; 

}

long fact(int n){
	long res = 1;
	for(int i=2;i<n+1;i++){
		res*=i;
	}
	return res;
}

void str_permute(char* final,char* a,int l,int r,int len){
	if(l==r){

		int last_index = 0;
		int i;
		while(final[last_index]!='\0'){
			last_index++;
		}
		//char* new_final = (char*) realloc(final,(last_index+10+len)*sizeof(char));
		if(final==NULL){
			printf("Null seen\n");
			exit(0);
		}
		
		for(i=last_index;i<(last_index+len);i++){
			*(final+i) = *(a+(i-last_index));

		}
		*(final+(last_index+len)) = '\0';
		
		//*final = *new_final;
		

	}else{
		int i;
		for(i=l;i<=r;i++){
			swap((a+l),(a+i));
			str_permute(final,a,l+1,r,len);
			swap((a+l),(a+i));
		}

	}
}

