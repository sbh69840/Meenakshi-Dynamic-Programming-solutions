#DISCLAIMER: THIS CODE IS FOR THE CASE WHEN YOU CAN MOVE ONLY RIGHT OR BOTTOM
m,n = map(int,input("Size of matrix").split())
arr = []
for a in range(m):
    arr.append(list(map(int,input().split())))
def min_cost(arr):
    cost = 0
    def minimum(arr,i,j):
        if i==m-1 and j==n-1:
            return arr[m-1][n-1]
        if i==m-1:
            return minimum(arr,i,j+1)+arr[i][j]
        if j==n-1:
            return minimum(arr,i+1,j)+arr[i][j]
            
        x = minimum(arr,i+1,j)
        y = minimum(arr,i,j+1)
        return min(x,y)+arr[i][j]
    cost=minimum(arr,0,0)
    return cost
def min_memo(arr):
    memo = []
    for a in range(len(arr)):
        memo.append([-1]*len(arr[0]))
    def minimum(arr,i,j):
        if memo[i][j]!=-1:
            return memo[i][j]
        if i==m-1 and j==n-1:
            memo[i][j]= arr[i][j]
        
        elif j==n-1:
            
            memo[i][j]= minimum(arr,i+1,j)+arr[i][j]
        elif i==m-1:
            memo[i][j] = minimum(arr,i,j+1)+arr[i][j]
        else:
            x = minimum(arr,i+1,j)
            y = minimum(arr,i,j+1)
            memo[i][j]= min(x,y)+arr[i][j]
        return memo[i][j]
    return minimum(arr,0,0)
#Without if-else the below code will not work because in this case, as we are
#returning the termination condition will not end if you don't follow the above
#code.
def min_memo1(arr):
    memo = []
    for a in range(len(arr)):
        memo.append([-1]*len(arr[0]))
    print(len(arr),len(arr[0]))
    def minimum(arr,i,j):
        if memo[i][j]!=-1:
            return memo[i][j]
        if i==m-1 and j==n-1:
            memo[i][j]= arr[i][j]
        if j==n-1:
            memo[i][j]= minimum(arr,i+1,j)+arr[i][j]
        if i==m-1:
            memo[i][j] = minimum(arr,i,j+1)+arr[i][j]
        
        x = minimum(arr,i+1,j)
        y = minimum(arr,i,j+1)
        memo[i][j]= min(x,y)+arr[i][j]
        return memo[i][j]
    return minimum(arr,0,0)
def dp(arr):
    memo = []
    for a in range(len(arr)):
        memo.append([0]*len(arr[0]))
    def minimum(arr):
        memo[0][0] = arr[0][0]
        for a in range(1,len(arr[0])):
            memo[0][a] = memo[0][a-1]+arr[0][a]
        for a in range(1,len(arr)):
            memo[a][0] = memo[a-1][0]+arr[a][0]
        for a in range(1,len(arr)):
            for b in range(1,len(arr[0])):
                memo[a][b] = min(memo[a-1][b],memo[a][b-1])+arr[a][b]
        return memo[len(arr)-1][len(arr[0])-1]
    return minimum(arr)
        
import time
#start = time.time()
#print(min_cost(arr),"Time taken for min_cost = %.10f"%(time.time()-start))
start = time.time()
#print(min_memo(arr),"Time taken for min_memo = %.20f"%(time.time()-start))
start = time.time()
print(dp(arr),"Time taken for dp = %.20f"%(time.time()-start))
        
    
