import time
class Paths:
	def __init__(self):
		pass
	class Memo:
		def __init__(self,fn):
			self.fn = fn
			self.memo = {}
		def __call__(self,*args):
			if args not in self.memo:
				self.memo[args] = self.fn(*args)
			return self.memo[args]

	@Memo
	def recursion(self):
		
	def dp(self):
		

	def solve(self):
		start = time.time()
		print("Recursion with memo time = ",self.recursion(self), time.time()-start)
		start = time.time()
		print("DP time = ",self.dp(self.x,self.y),time.time()-start)
		


path = Paths()
path.solve()

