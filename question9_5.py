a = input("Enter string 1")
b = input("Enter string 2")

c = a+b
c = list(c)
def swap(c,l,i):
	tmp = c[i]
	c[i] = c[l]
	c[l] = tmp
	return c
def fact(n):
	res = 1
	for a in range(2,n+1):
		res*=a
	return res
perm = []
def permutations(c,l,r):
	if (l==r):
		perm.append(''.join(c))
	else:
		for i in range(l,r+1):
			c[l],c[i] = c[i],c[l]
			permutations(c,l+1,r)
			c[l],c[i] = c[i],c[l]
def perm_iter(c):
	prev_layer = [c]
	for i in range(0,len(c)):
		new_prev = []
		for j in range(i,len(c)):
			for a in prev_layer:
				b = a.copy()
				new_prev.append(swap(b,i,j))
		prev_layer = new_prev
	return prev_layer
import time
start = time.time()
# res= perm_iter(c)
# print("Time taken = ",time.time()-start)

# for a in res:
# 	print(''.join(a))

def johnson_trotter(c):
	perm = []
	left_to_right = True
	right_to_left = False
	def get_mobile(arr,dir,n):
		mobile_prev = 0
		mobile = 0
		for i in range(n):
			if (dir[arr[i]-1]==right_to_left and i!=0):
				if arr[i]>arr[i-1] and arr[i]>mobile_prev:
					mobile=arr[i]
					mobile_prev=mobile 
			if(dir[arr[i]-1]==left_to_right and i!=n-1):
				if arr[i]>arr[i+1] and arr[i]>mobile_prev:
					mobile=arr[i]
					mobile_prev=mobile 
		if mobile==0 and mobile_prev ==0:
			return 0
		else:
			return mobile 
	def getOnePerm(arr,dir,n):
		
		mobile = get_mobile(arr,dir,n)
		
		try:
			pos = arr.index(mobile)
			if(dir[arr[pos]-1]==left_to_right):
				swap(arr,pos,pos+1)
			elif(dir[arr[pos]-1]==right_to_left):
				swap(arr,pos,pos-1)
		except:
			pass
		for i in range(n):
			if (arr[i]>mobile):
				if(dir[arr[i]-1]==left_to_right):
					dir[arr[i]-1]=right_to_left
				elif(dir[arr[i]-1]==right_to_left):
					dir[arr[i]-1]=left_to_right

		print(" | ",arr," | ")
	def solve():
		arr = [2,2,1,1,2,2,1]
		# for a in range(len(c)):
		# 	arr.append(a+1)
		dir = [right_to_left]*len(arr)
		n = len(arr)
		perm.append(arr.copy())
		for i in range(1,3):
			getOnePerm(arr,dir,n)

			
	solve()
	return perm 
start = time.time()
res = johnson_trotter(c)
print("Time taken = ",time.time()-start)
asd = asd
start = time.time()
permutations(c,0,len(c)-1)
print("Time taken = ",time.time()-start)
# print(perm)
asd=asd
def interleaving(str1,str2,str3):
	if (len(str3)!=(len(str1)+len(str2))):
		return False
	dp = []
	for a in range(len(str1)+1):
		dp.append([False]*(len(str2)+1))
	dp[0][0] = True
	for a in range(1,len(str1)+1):
		if (str1[a-1]!=str3[a-1]):
			dp[a][0] = False
		else:
			dp[a][0] = dp[a-1][0]
	for a in range(1,len(str2)+1):
		if (str2[a-1]!=str3[a-1]):
			dp[0][a] = False
		else:
			dp[0][a] = dp[0][a-1]
	for a in range(1,len(str1)+1):
		for b in range(1,len(str2)+1):
			if (str1[a-1]==str2[b-1] and (str1[a-1]==str3[a+b-1])):
				dp[a][b] = (dp[a-1][b] or dp[a][b-1])
			elif (str1[a-1]==str3[a+b-1]):
				dp[a][b] = dp[a-1][b]
			elif (str2[b-1]==str3[a+b-1]):
				dp[a][b] = dp[a][b-1]
			else:
				dp[a][b] = False
	return dp[len(str1)][len(str2)]
print("All the interleaving permutations of the addition of two strings are")
for i in perm:
	if (interleaving(a,b,i)):
		print(" | ",i," | ")




