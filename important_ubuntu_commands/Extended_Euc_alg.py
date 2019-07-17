class Extended_Euclidean:
	def __init__(self,a,b):
		self.a = a
		self.b = b
	def solve(self):
		x = 0;x1 = 1
		y = 1;y1 = 0
		r = self.b;r1 = self.a
		while r!=0:
			quotient = r1//r
			r1,r = r,r1-(quotient*r)
			x1,x = x,x1-(quotient*x)
			y1,y = y,y1-(quotient*y)
		return r1,x1,y1
print(Extended_Euclidean(24,18).solve())