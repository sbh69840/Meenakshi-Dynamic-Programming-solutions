import math
class Minimum_weights:
	def __init__(self,n):
		self.n = n
		self.count = 0
		self.weights = 0
	def print_weights(self):
		print("Minimum weights = ",self.count+self.weights)
		for i in range(self.count):
			print(3**i,end=" ")
		if self.weights!=0:
			print(self.weights,end=" ")
	def solve(self):
		max_3_pow = math.floor(math.log10(self.n)/math.log10(3))
		sum_3_series = int((3**(max_3_pow+1)-1)/2)
		self.count = max_3_pow+1
		self.weights=0 if (self.n-sum_3_series)<=0 else (self.n-sum_3_series)
		self.print_weights()
	def solve_unop(self):
		res=0
		count=0
		while True:
			pow_3 = 3**count
			res+=pow_3
			if pow_3>n:
				res-=pow_3
				break
			count+=1
		if self.n-res<=0:
			self.count=count
			return
		self.weights = self.n-res 
		self.count=count


if __name__=="__main__":
	n = int(input())
	Minimum = Minimum_weights(n)
	

