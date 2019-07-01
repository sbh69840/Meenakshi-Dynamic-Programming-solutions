import time
str1 = input("Enter string1")
str2 = input("Enter string2")
class Memoize:
	def __init__(self,fn):
		self.fn = fn
		self.memo = {}
	def __call__(self,*args):
		if args not in self.memo:
			self.memo[args]=self.fn(*args)
		return self.memo[args]

@Memoize
def editDistance(str1,str2):
	if len(str1)==0:
		return len(str2)
	if len(str2)==0:
		return len(str1)
	if str1[0]==str2[0]:
		return editDistance(str1[1:],str2[1:])
	d = editDistance(str1[1:],str2)
	u = editDistance(str1[1:],str2[1:])
	i = editDistance(str1,str2[1:])
	return min(d,u,i)+1
def solve_memo(str1,str2):
	memo = []
	c = len(str1)
	d = len(str2)
	for a in range(c+2):
		memo.append([-1]*(d+2))
	def editDistance(str1,str2):
		n = len(str1)
		m = len(str2)
		if memo[n][m]!=-1:
			return memo[n][m]
		if n==0:
			memo[n][m]=m
			return memo[n][m]
		if m==0:
			memo[n][m]=n
			return memo[n][m]
		if str1[0]==str2[0]:
			memo[n][m]=editDistance(str1[1:],str2[1:])
			return memo[n][m]
		d = editDistance(str1[1:],str2)
		u = editDistance(str1[1:],str2[1:])
		i = editDistance(str1,str2[1:])
		memo[n][m]=min(d,u,i)+1
		return memo[n][m]
		
	editDistance(str1,str2)
	return memo[c][d]

def solve_dp(str1,str2,n,m):
	memo = [[0 for a in range(m+1)]for b in range(n+1)]
	for a in range(n):
		memo[a][0] = a
	for a in range(m):
		memo[0][a] = a
	for i in range(1,n+1):
		for j in range(1,m+1):
			if(str1[i-1]==str2[j-1]):
				memo[i][j] = memo[i-1][j-1]
			else:
				memo[i][j] = min(memo[i-1][j-1],memo[i][j-1],memo[i-1][j])+1
	return memo[n][m]


start = time.time()
print(editDistance(str1,str2)," Time Dec_memo = ",time.time()-start)
start = time.time()
print(solve_memo(str1,str2)," Time Norm_memo = ",time.time()-start)
start = time.time()
print(solve_dp(str1,str2,len(str1),len(str2))," Time DP = ",time.time()-start)

