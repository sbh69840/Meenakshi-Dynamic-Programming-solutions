primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71]
def unique_primes(num):
	res = 0
	for a in primes:
		if num%a==0:
			res+=1
		while num%a==0:
			num = num/a
	return res
def product(arr):
	res = 1
	for i in arr:
		res*=i
	return res
def solve(arr,n,k,s):
	max_res = 0
	for i in range(n):
		for j in range(i+1,n+1):
			sub_prod = product(arr[i:j])
			p = unique_primes(sub_prod)
			res = sum(arr[i:j])*(k-p*s)
			if res>max_res:
				max_res=res
	return max_res
n,k,s = input().split(" ")
n = int(n)
k = int(k)
s = int(s)
# n,k,s = map(int,input().split())
arr = list(map(int,input().split()))
print(solve(arr,n,k,s))
