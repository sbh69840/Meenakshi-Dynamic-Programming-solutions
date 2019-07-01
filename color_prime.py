primes = [2,3,5,7,11,13]
def unique_primes(n,unique):
	res=0
	if n<2:
		return 0
	for a in primes:
		if n%a==0:
			unique.append(a)
			res+=1
			while n%a!=0:
				n/=a
	return res
k = int(input())
n = int(input())
arr = list(map(int,input().split()))
def product(arr):
	res = 1
	for a in arr:
		res*=a
	return res
def solve(arr,k,n):
	unique = []
	res =0
	uni_count = unique_primes(product(arr),unique)
	print(unique,uni_count)
	for i in unique:
		for j in range(1,len(arr)):
			if not (arr[j-1]%i==0 and arr[j]%i==0) or (not (arr[j-1]%i!=0 and arr[j]%i!=0)):
				res+=1
	print(res)
solve(arr,k,n)