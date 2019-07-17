#Longest Monotonically Increasing subsequence DP to print the longest subsequence
#Whenever we find that there is another subarray at j'th index whose length is
#greater than the current one at i'th index, then we replace the subarray at i'th
#index with the j'th index. And after coming out of the loop we add the element of the
#array at i'th index because it is not added during comparision.
 
def LIS(arr,n):
	print_lis[0].append(arr[0])
	for i in range(1,n):
		for j in range(0,i):
			if arr[j]<arr[i] and len(print_lis[j])>len(print_lis[i]):
				print_lis[i]=print_lis[j].copy()
		print_lis[i].append(arr[i])
arr = [1,2,3,4,2,6]
print_lis = [[] for _ in range(len(arr))]
LIS(arr,len(arr))
print(print_lis) 