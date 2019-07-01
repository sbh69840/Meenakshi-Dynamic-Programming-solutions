class Memo:
	def __init__(self,fn):
		self.fn = fn
		self.memo = {}
	def __call__(self,*args):
		if args not in self.memo:
			self.memo[args]=self.fn(*args)
		return self.memo[args]

@Memo
def recursion(s1,s2):
	if len(s1)==0 or len(s2)==0:
		return 0
	if s1[-1]==s2[-1]:
		
		res1 =  recursion(s1[:-1],s2[:-1])+1
		print(prev,res1)
		if res1>prev:
			LCS.append(s1[-1])
		return res1
	first = recursion(s1[:-1],s2)
	second = recursion(s1,s2[:-1])
	res = max(first,second)
	if prev<res:
		prev=res
	return res

class solve_recur:
	def __init__(self,s1,s2):
		self.s1 = s1
		self.s2 = s2
		self.LCS = []
		self.prev = 0
		self.solve()
	@Memo
	def recursion(self,s1,s2):
		if len(s1)==0 or len(s2)==0:
			return 0
		if s1[-1]==s2[-1]:
			res1 =  self.recursion(self,s1[:-1],s2[:-1])+1
			return res1
		first = self.recursion(self,s1[:-1],s2)
		second = self.recursion(self,s1,s2[:-1])
		res = max(first,second)
		return res
	def dp(self,s1,s2):
		a = len(s1)
		b = len(s2)
		memory = [[0 for _ in range(b+1)] for _ in range(a+1)]
		for i in range(1,a+1):
			for j in range(1,b+1):
				if s1[i-1]==s2[j-1]:

					memory[i][j] = memory[i-1][j-1]+1
				else:
					memory[i][j] = max(memory[i][j-1],memory[i-1][j])
		return memory[a][b],memory
	def find_lcs(self,s1,s2):
		lcs_len,lcs_count = self.dp(self.s1,self.s2)
		self.LCS = [0]*lcs_len
		a = len(s1)
		b = len(s2)
		i = a
		j = b
		lcs_len-=1
		while(i>0 and j>0):
			if s1[i-1]==s2[j-1]:
				self.LCS[lcs_len] = s1[i-1]
				i-=1
				j-=1
				lcs_len-=1
			elif (lcs_count[i-1][j]>lcs_count[i][j-1]):
				i-=1
			else:
				j-=1
		return len(self.LCS)
	def solve(self):
		print("Recursion solution = ",self.recursion(self,self.s1,self.s2))
		print("DP = ",self.find_lcs(self.s1,self.s2))
		print("LCS = ",self.LCS," Length = ",len(self.LCS))


s1 = "AAACCGTGAGTTATTCGTTCTAGAA"
s2 = "CACCCCTAAGGTACCTTTGGTTC"

def dp(s1,s2):
	a = len(s1)
	b = len(s2)
	memory = [[0 for _ in range(b+1)] for _ in range(a+1)]
	for i in range(1,a+1):
		for j in range(1,b+1):
			if s1[i-1]==s2[j-1]:
				memory[i][j] = memory[i-1][j-1]+1
			else:
				memory[i][j] = max(memory[i][j-1],memory[i-1][j])
	print(memory)
	return memory[a][b]



# s1 = "AAACCGTGA"
# s2 = "CACCCCTAAG"

# s1 = "ABCD"
# s2 = "AEBD"

# s1 = "ABCD"
# s2 = "BCCD"

print(solve_recur(s1,s2))
