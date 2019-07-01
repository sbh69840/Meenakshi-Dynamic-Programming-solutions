n = int(input())
def recursion(n):
    def solve(n):
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 2
        return solve(n-1)+solve(n-2)
    return solve(n)
def memo(n):
    memo = [-1]*(n)
    def solve(n):
        if memo[n-1]!=-1:
            return memo[n-1]
        if n==1:
            return 1
        if n==2:
            return 2
        memo[n-1]=solve(n-1)+solve(n-2)
        return memo[n-1]
    return solve(n)
def dp(n):
    memo = [-1]*(n)
    def solve(n):
        memo[0]=1
        memo[1]=2
        for a in range(2,n):
            memo[a]=memo[a-1]+memo[a-2]
        return memo[n-1]
    return solve(n)
import time
#start = time.time()
#print(recursion(n),time.time()-start)
start = time.time()
print(memo(n),time.time()-start)
start = time.time()
print(dp(n),time.time()-start)

