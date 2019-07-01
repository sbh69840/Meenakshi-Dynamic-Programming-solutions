#Longest monotonically increasing (LMI) subsequence of an array of integers
#Another approach would be to generate all the sequences and look for the
#LMI subsequence, but that would prove costly as the time complexity is O(2^n) 
#for generating and O(n) time for checking monotonically increasing for each
#subsequence generated to find the maximum length.
#Therefore, the algorithm below, does not evaluate for the cases where the 
#subarray is not monotonically increasing. 
def recursion(arr,index,subarr):
	if index==len(arr):
		print(subarr)
		return len(subarr)
	else:
		if len(subarr)>0:
			if arr[index]>subarr[-1]:
				first = recursion(arr,index+1,subarr)
				second = recursion(arr,index+1,subarr+[arr[index]])
			else:
				first = recursion(arr,index+1,subarr)
				#When the element at that index is not in an increasing order,
				#Then the length of that particular subarray is 0
				second = 0
		else:
			first = recursion(arr,index+1,subarr)
			second = recursion(arr,index+1,subarr+[arr[index]])
		return max(first,second)

print((recursion([1,6,2,5,3,4,5],0,[])))

