m,n = map(int,input().split())
arr = []
for a in range(m):
    arr.append(list(map(int,input().split())))
def min_cost(arr):
    cost = 0
    def minimum(arr,i,j):
        if i==m-1 and j==n-1:
            return arr[i][j]
        if i==m-1:
            return minimum(arr,i,j+1)+arr[i][j]
        if j==n-1:
            return min(minimum(arr,i+1,j),minimum(arr,i+1,j-1))+arr[i][j]
        if j==0:
            return min(minimum(arr,i+1,j),minimum(arr,i,j+1),minimum(arr,i+1,j+1))\
                   +arr[i][j]
        x = minimum(arr,i,j+1)
        y = minimum(arr,i+1,j)
        z = minimum(arr,i+1,j+1)
        z_ = minimum(arr,i+1,j-1)
        return min(x,y,z,z_)+arr[i][j]
    cost = minimum(arr,0,0)
    return cost
def min_memo(arr):
    memo = []
    for a in range(len(arr)):
        memo.append([0]*len(arr[0]))
    def minimum(arr,i,j):
        if memo[i][j]!=0:
            return memo[i][j]
        if i==m-1 and j==n-1:
            return arr[i][j]
        elif i==m-1:
            memo[i][j]=minimum(arr,i,j+1)+arr[i][j]
        elif j==n-1:
            memo[i][j]=min(minimum(arr,i+1,j),minimum(arr,i+1,j-1))+arr[i][j]
        elif j==0:
            memo[i][j]=min(minimum(arr,i+1,j),minimum(arr,i,j+1),minimum(arr,i+1\
                                                                         ,j+1))+\
                                                                         arr[i][j]
        else:
            x = minimum(arr,i,j+1)
            y = minimum(arr,i+1,j)
            z = minimum(arr,i+1,j+1)
            z_ = minimum(arr,i+1,j-1)
            memo[i][j]=min(x,y,z,z_)+arr[i][j]
        return memo[i][j]
    return minimum(arr,0,0)
def min_dp(arr):
    memo = []
    for a in range(len(arr)+2):
        memo.append([0]*(len(arr[0])+2))
    def minimum(arr):
        r = len(arr)
        c = len(arr[0])
        memo[r][c]=3
        for a in range(c-1,0,-1):
            memo[r][a]=memo[r][a+1]+arr[r-1][a-1]
        for a in range(r-1,0,-1):
            for b in range(c,0,-1):
                n_ar = memo[a][b+1],memo[a+1][b],memo[a+1][b+1]\
                               ,memo[a+1][b-1]
                memo[a][b]=min([n for n in n_ar if n!=0])+arr[a-1][b-1]
        return memo[1][1]
    return minimum(arr)
            
import time
#start = time.time()
#print(min_cost(arr),"Time taken for min_cost = %.10f"%(time.time()-start))
start = time.time()
print(min_memo(arr),"Time taken for min_memo = %.10f"%(time.time()-start))

start = time.time()
print(min_dp(arr),"Time taken for dp = %.20f"%(time.time()-start))
