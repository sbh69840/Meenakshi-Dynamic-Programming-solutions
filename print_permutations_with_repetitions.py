#Given a places, fill it with n-distinct digits with repetitions allowed.
distinct = [1,3,4]
a = 2
n = len(distinct)
def permuts(arr,n,m,a):
	if m==a:
		print(arr)
		return
	for b in range(0,n):
		arr[m] = distinct[b]
		permuts(arr,n,m+1,a)			
permuts([0,0],n,0,a)