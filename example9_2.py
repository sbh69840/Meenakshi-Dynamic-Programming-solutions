#The question is to find total path from top left to bottom right of a matrix if you can only move down or right
import time
import cProfile
n = int(input())

class Memoize:
	def __init__(self,fn):
		self.memo = {}
		self.fn = fn
	def __call__(self,*args):
		if args not in self.memo:
			self.memo[args]=self.fn(*args)
		return self.memo[args]


@Memoize
def solve(i,j):
	if i==n-1 and j==n-1:
		return 0
	if i==n-1 or j==n-1:
		return 1
	return solve(i+1,j)+solve(i,j+1)
def solve1(i,j):
	if i==0 and j==0:
		return 0
	if i==0 or j==0:
		return 1
	return solve1(i-1,j)+solve1(i,j-1)

def dp(n):
	memo = []
	for a in range(n):
		memo.append([0]*n)
	for a in range(n-1,-1,-1):
		memo[a][n-1]=1
		memo[n-1][a]=1
	memo[n-1][n-1] = 0
	for a in range(n-2,-1,-1):
		for b in range(n-2,-1,-1):
			memo[a][b] = memo[a+1][b]+memo[a][b+1]
	return memo[0][0]
def fact(n):
	res = 1
	for a in range(2,n+1):
		res = (res*a)%1000000007
	return res
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y
def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m
def ncr(n,r):
	a = fact(n)
	b = (fact(n-r)*fact(r))%1000000007
	inv = modinv(b,1000000007)
	return (inv*a)%1000000007



if __name__=="__main__":
	#start = time.time()
	#print(solve(0,0)," Time for memo = ",time.time()-start)
	#start = time.time()
	#print(solve1(n-1,n-1)," Time without memo = ",time.time()-start)
	start = time.time()
	print(dp(n)," Time for DP = ",time.time()-start)
	start = time.time()
	print(ncr(2*(n-1),n-1)," Time for nCr = ",time.time()-start)



