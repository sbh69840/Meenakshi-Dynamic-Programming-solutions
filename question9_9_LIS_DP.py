#Longest Monotonically Increasing subsequence length
def LIS(arr,n):
    max_length = 1
    dp = [1]*n
    for i in range(1,n):
        for j in range(0,i):
            if arr[j]<arr[i] and dp[j]+1>dp[i]:
                dp[i]=dp[j]+1
        print_subarr[i].append(arr[i])
        max_length = max(max_length,dp[i])
        
    return max_length 
arr = [1,2,3,5,4,1,2,3,4,5,6,7,4,2,3,5]
print_subarr = [[] for _ in range(len(arr))]
print(LIS(arr,len(arr)))
print(print_subarr)