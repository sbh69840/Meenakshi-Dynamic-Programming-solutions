#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int editDistance(char*,char*);
int getMin(int,int,int);
int solve_memo(char*,char*);
int solve_dp(char*,char*,int,int);
int main()
{
    char str1[100];
    char str2[100];
    printf("Enter string 1");
    scanf("%s",str1);
    printf("Enter string 2");
    scanf("%s",str2);
    //printf("Result = %d\n",editDistance(str1,str2));

    printf("Memo = %d\n",solve_memo(str1,str2));
    printf("DP = %d\n",solve_dp(str1,str2,strlen(str1),strlen(str2)));
    return 0;
}
int getMin(int a,int b,int c){
    int min = a;
    if(a<b && b<=c){
        min=a;
    }else if(b<c){
        min=b;
    }else{
        min=c;
    }
    return min;
    
    

}
int editDistance(char* str1,char* str2){
    if(str1==NULL||*str1=='\0'){
        return strlen(str2);
    }
    if(str2==NULL || *str2=='\0'){
        return strlen(str1);
    }
    if(*str1==*str2){
        return editDistance(str1+1,str2+1);
    }
    int d,u,i;
    d = editDistance(str1+1,str2);
    u = editDistance(str1+1,str2+1);
    i = editDistance(str1,str2+1);
    return getMin(d,u,i)+1;

}

int solve_memo(char* str1,char* str2){
    int n = strlen(str1);
    int m = strlen(str2);
    int memo[n+2][m+2];
    for(int i=0;i<n+2;i++){
        for(int j=0;j<m+2;j++){
            memo[i][j]=-1;
        }
    }
    auto int editDistance(char*,char*);
    int editDistance(char* str1,char* str2){
        int a = strlen(str1);
        int b = strlen(str2);
        if(memo[a][b]!=-1){
            return memo[a][b];
        }
        if(str1==NULL||*str1=='\0'){
            memo[0][b] = b;
            return memo[0][b];
        }
        if(str2==NULL||*str2=='\0'){
            memo[a][0] = a;
            return memo[a][0];
        }
        if(*str1==*str2){
            memo[a][b] = editDistance(str1+1,str2+1);
            return memo[a][b];
        }
        int d,u,i;
        d = editDistance(str1+1,str2);
        u = editDistance(str1+1,str2+1);
        i = editDistance(str1,str2+1);
        memo[a][b] = getMin(d,u,i)+1;
        return memo[a][b];
    } 
    
    return editDistance(str1,str2);
}

int solve_dp(char* s1,char* s2,int m,int n){
    int memo[m+1][n+1];
    for(int i=0;i<=n;i++)memo[0][i]=i;
    for(int i=0;i<=m;i++)memo[i][0]=i;
    for(int i=1;i<=m;i++){
        for(int j=1;j<=n;j++){
            if(s1[i-1]==s2[j-1]){
                memo[i][j]=memo[i-1][j-1];
            }else{
                memo[i][j] = getMin(memo[i-1][j-1],memo[i-1][j],memo[i][j-1])+1;
            }
        }
    }
    for(int i=0;i<=m;i++){
        for(int j=0;j<=n;j++){
            printf("%d ",memo[i][j]);
        }
        printf("\n");
    }
    return memo[m][n];
}