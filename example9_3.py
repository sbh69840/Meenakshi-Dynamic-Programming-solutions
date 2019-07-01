str1 = input("Enter string1")
str2 = input("Enter string2")
str3 = input("Enter string3 to check interleaving between 1 and 2")
class Memo:
	def __init__(self,fn):
		self.fn = fn
		self.memo = {}
	def __call__(self,*args):
		if args not in self.memo:
			self.memo[args] = self.fn(*args)
		return self.memo[args]
@Memo
def recursion(str1,str2,str3):
	if len(str3)!=(len(str1)+len(str2)):
		return False
	if len(str1)==0 and len(str2)==0 and len(str3)==0:
		return True
	if len(str3)==0:
		return False
	if len(str1)==0 and len(str2)==0:
		return False

	first = False
	second = False
	if(len(str1)!=0 and str1[0]==str3[0]):
		first = recursion(str1[1:],str2,str3[1:])
	if(len(str2)!=0 and str2[0]==str3[0]):
		second = recursion(str1,str2[1:],str3[1:])
	return first or second
def dp(str1,str2,str3):
	a = len(str1)
	b = len(str2)
	c = len(str3)

	if (c!=(b+a)):
		return False
	memo = []
	for d in range(a+1):
		memo.append([False]*(b+1))
	memo[0][0]=True
	for d in range(1,a+1):
		if str1[d-1]!=str3[d-1]:
			memo[d][0]=False
		else:
			memo[d][0]=memo[d-1][0]
	for d in range(1,b+1):
		if str2[d-1]!=str3[d-1]:
			memo[0][d]=False
		else:
			memo[0][d]=memo[0][d-1]
	
	for d in range(1,a+1):
		for e in range(1,b+1):
			if (str1[d-1]==str2[e-1] and (str1[d-1]==str3[d+e-1])):
				memo[d][e] = memo[d-1][e] or memo[d][e-1]
			elif (str1[d-1]==str3[d+e-1]):
				memo[d][e] = memo[d-1][e]
			elif (str2[e-1]==str3[d+e-1]):
				memo[d][e] = memo[d][e-1]
			else:
				memo[d][e]=False
	
	return memo[a][b]

#During the case when the two strings are different
def dp_diff(str1,str2,str3):
	a = len(str1)
	b = len(str2)
	c = len(str3)

	if(c!=(a+b)):
		return False
	count1 = 0
	count2 = 0
	for i in range(c):
		
		if count1<a and str3[i]==str1[count1]:
			count1+=1
		elif count2<b and str3[i]==str2[count2]:
			count2+=1
	if count1==(a) and count2==(b):
		return True
	else:
		return False



print("Recursion = ",recursion(str1,str2,str3))
print("Dp = ",dp(str1,str2,str3))
print("DP with both strings different ",dp_diff(str1,str2,str3))
