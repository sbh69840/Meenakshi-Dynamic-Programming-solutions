def k_divisible(arr,n,k):
	mod = [0]*k
	sub_sum = 0
	for a in  range(n):
		sub_sum = sub_sum+arr[a]
		mod[sub_sum%k] = mod[sub_sum%k]+1
	result = 0
	for a in mod:
		result+=(a*(a-1))//2
	return result+mod[0]
print(k_divisible([1,2,3,4],4,1))