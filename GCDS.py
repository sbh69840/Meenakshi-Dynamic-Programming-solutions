def GCD(x,y):
	while(y):
		x,y=y,x%y
	return x
def gcd_seq(arr):
	result = arr[0]
	for i in range(1,len(arr)):
		result = GCD(result,arr[i])
	return result
def n_sum(n):
	return int((n*(n+1))/2)
n = int(input())
arr = list(map(int,input().split()))

longest_j = 0
longest_i = 0

gcd_exists = [0]*n
last_j = 0
j_count = 0
j_max = 0
gcd_prev = arr[0]
gcd_cur = 0
for i in range(n):
	gcd_prev = arr[i]
	for j in range+.(i,n):
		gcd_cur = GCD(gcd_prev,arr[j])
		if gcd_cur>1:
			j_count+=1
			last_j = j
			gcd_exists[i]=gcd_cur 
			gcd_exists[j]=gcd_cur
		gcd_prev = gcd_cur

	if j_count>j_max:
		j_max=j_count
		longest_i = i
		longest_j = last_j
	j_count=0



# for i in range(n):
# 	for j in range(n):
# 		print(gcds[i][j],end=" ")
# 	print()
current_max = n+n_sum(longest_j-longest_i)
if longest_i-2>=0:
	a = gcd_exists[longest_i-2]
	if a!=0 and a==gcd_exists[longest_i]:
		ind = longest_i-2
		while ind>0:
			if gcd_exists[ind]==a:
				ind-=1
			else:
				break
		new_max = n+n_sum(longest_j-ind)
		if new_max>current_max:
			current_max=new_max
	elif a!=0 and a*gcd_exists[longest_i]<(5*(10)^5):
		ind = longest_i-2
		while ind>0:
			if gcd_exists[ind]==a:
				ind-=1
			else:
				break
		new_max = n+n_sum(longest_j-longest_i+1)+n_sum(longest_i-ind-1)
		if new_max>current_max:
			current_max=new_max
if longest_j+2<n:
	a = gcd_exists[longest_j+2]
	if a!=0 and a==gcd_exists[longest_j]:
		ind = longest_j+2
		while ind<n-1:
			if gcd_exists[ind]==a:
				ind+=1
			else:
				break
		new_max = n+n_sum(ind-longest_i)
		if new_max>current_max:
			current_max=new_max
	elif a!=0 and a*gcd_exists[longest_j]<=(5*(10)^5):
		ind = longest_j+2
		while ind<n-1:
			if gcd_exists[ind]==a:
				ind+=1
			else:
				break
		new_max = n+n_sum(longest_j-longest_i+1)+n_sum(ind-longest_j-1)
		if new_max>current_max:
			current_max=new_max

if longest_i-2>=0:
	if arr[longest_i-2]*gcd_exists[longest_i]<=(5*(10)^5):
		new_max = n+n_sum(longest_j-longest_i+1)+1
		if new_max>current_max:
			current_max=new_max
if longest_j+2<n:
	if arr[longest_j+2]*gcd_exists[longest_j]<=(5*(10)^5):
		new_max = n+n_sum(longest_j-longest_i+1)+1
		if new_max>current_max:
			current_max=new_max
print(current_max)
