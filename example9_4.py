import time
class Subset_sum:
	def __init__(self,v,coins):
		self.coins = coins
		self.v = v
		self.subset = []
		self.prev = 0
		self.solve()
		print(self.subset)
	class Memo:
		def __init__(self,fn):
			self.fn = fn
			self.memo = {}
		def __call__(self,*args):
			if args not in self.memo:
				self.memo[args] = self.fn(*args)
			return self.memo[args]
	
	def recursion(self,coins,v):
		if v==0:
			return True
		if len(coins)==0:
			return False
		if coins[0]>v:
			return self.recursion(coins[1:],v)
		res =  self.recursion(coins[1:],v) or self.recursion(coins[1:],v-coins[0])
		if res==True:
			if self.prev!=v:
				self.subset.append(coins[0])
			self.prev = v
		return res

	def dp(self):
		memory = []
		for a in range(len(self.coins)+1):
			memory.append([False]*(v+1))
		for i in range(len(self.coins)+1):
			memory[i][0]=True
		for i in range(1,v+1):
			memory[0][i] = False
		for i in range(1,len(self.coins)+1):
			for j in range(1,v+1):
				if memory[i-1][j]==True:
					memory[i][j] = True
				if j-self.coins[i-1]>=0 and j-self.coins[i-1]<=v and memory[i-1][j-self.coins[i-1]]==True:
					memory[i][j] = True
		return memory[len(self.coins)][v]
	def solve(self):
		start = time.time()
		print("The recursion = ",time.time()-start," Result = ",self.recursion(self.coins,self.v))
		start = time.time()
		print("The DP time = ",time.time()-start," Result = ",self.dp())

v = 15
coins = [7,3,5,7,1,4,2]
res = Subset_sum(v,coins)



