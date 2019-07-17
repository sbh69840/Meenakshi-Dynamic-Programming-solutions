#Longest Increasing Subsequence
maximum = 1

def LIS(arr,n):
    if n==1:
        return 1
    max_length_until_now = 1
    for i in range(1,n):
        result = LIS(arr,i)
        if arr[i-1]<arr[n-1] and result+1>max_length_until_now:
            max_length_until_now=result+1
    global maximum
    maximum = max(maximum,max_length_until_now)
    return max_length_until_now
arr = [1,2,3,5,4,1,2,3,4,5,6,7,4,2,3,5] 
LIS(arr,len(arr))
print(maximum)
print(print_subarr)

