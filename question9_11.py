#Longest bitonic sequence. For example,
#{1,4,6,8,3,-2} is bitonic, but {1,4,6,2,-1,10} is not bitonic.
maximum = 0
def LBS(arr,n):
	if n==1:
		return 1,1
	max_lis_n = 1
	max_lds_n = 1
	for a in range(1,n):
		result1,result2 = LBS(arr,a)
		if arr[a-1]<arr[n-1] and result1+1>max_lis_n:
			max_lis_n=result1+1
		if arr[a-1]>arr[n-1] and result2+1>max_lds_n:
			max_lds_n=result2+1
	global maximum
	maximum=max(maximum,max_lis_n+max_lds_n-1)
	return max_lis_n,max_lds_n
arr = [0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
print(LBS(arr,len(arr)))
print(maximum)