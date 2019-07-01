#The code below if for subsequence
def LCS(arr,n):
	s = set()
	for a in arr:
		s.add(a)
	ans = 0
	for a in range(n):
		if arr[a]-1 not in s:
			j = arr[a]
			while j in s:
				j+=1
			ans = max(ans,j-arr[a])
	return ans
def LCS_subarray(arr,n):
	ans = 1
	res = 0
	for a in range(n-1):
		if arr[a]==(arr[a+1]-1):
			ans+=1
		else:
			ans=1
		res = max(ans,res)
	return res
print("Longest consecutive subsequence = ",LCS([5,1,2,3,4,0],6))
print("Longest consecutive subarray = ",LCS_subarray([5,1,2,3,4,0],6))




		
