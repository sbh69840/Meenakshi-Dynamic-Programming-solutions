import time
class Paths:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	class Memo:
		def __init__(self,fn):
			self.fn = fn
			self.memo = {}
		def __call__(self,*args):
			if args not in self.memo:
				self.memo[args] = self.fn(*args)
			return self.memo[args]

	@Memo
	def recursion(self,x,y):
		if x==0 or y==0:
			return 1
		if x==0 and y==0:
			return 0
		return self.recursion(self,x-1,y)+self.recursion(self,x,y-1)
	def dp(self,x,y):
		memo = []
		for i in range(x+1):
			memo.append([0]*(y+1))
		for i in range(x+1):
			memo[i][0] = 1
		for j in range(y+1):
			memo[0][j] = 1
		memo[0][0] = 1
		for i in range(1,x+1):
			for j in range(1,y+1):
				memo[i][j] = memo[i-1][j]+memo[i][j-1]
		return memo[x][y]
	def block(self):
		self.blocks = []
		print("Enter the coordinates to block or enter 0 to quit")
		while True:
			from_ = list(map(int,input("Enter the from coordinates of horizontal road\n").split()))
			if len(from_)==1:
				break
			to_ = list(map(int,input("Enter the to coordinates along the road of from\n").split()))
			if from_[0]==to_[0]:
				for a in range(from_[1],to_[1]):
					self.blocks.append([from_[0],a])

			else:
				print("Enter the right coordinates.")
				continue
	def dp_with_block(self,x,y):
		memo = []
		for i in range(x+1):
			memo.append([-1]*(y+1))
		for i in range(x+1):
			memo[i][0] = 1
		for j in range(y+1):
			memo[0][j] = 1

		memo[0][0] = 0
		print("Blocks ",self.blocks)
		for a in self.blocks:
			memo[a[0]][a[1]] = 0
		for i in range(1,x+1):
			for j in range(1,y+1):
				if memo[i][j]!=0:
					memo[i][j] = memo[i-1][j]+memo[i][j-1]
		return memo[x][y]

	def solve(self):
		start = time.time()
		print("Recursion with memo time = ",self.recursion(self,self.x,self.y), time.time()-start)
		start = time.time()
		print("DP time = ",self.dp(self.x,self.y),time.time()-start)
		self.block()
		start = time.time()
		print("DP with block = ",self.dp_with_block(self.x,self.y),time.time()-start)


path = Paths(int(input("Enter x\n")),int(input("Enter y\n")))
path.solve()

