#Later on I figured out that the below recursive code does not give the right answer
#because if I say end on count >=2 it means that I am checking if the sum exists in 
#the subset of an array of size 2. In short iF i give and array with size 2 and sum 
#is a element in the array, the function will return true even if the value is present in 
#one element of the array
def recursion(coins,v,count):
	if v==0:
		print(coins)
		return True
	if len(coins)==0:
		return False
	if coins[0]>v:
		recursion(coins[1:],v,count)
	return recursion(coins[1:],v-coins[0],count+1) or recursion(coins[1:],v,count)

#The below solution is o(n^2)

def iterative(coins,v):
	coin1 = 0
	coin2 = 0
	for a in range(len(coins)):
		for b in range(a+1,len(coins)):
			if (coins[a]+coins[b])==v:
				coin1 = coins[a]
				coin2 = coins[b]
	return coin1,coin2


#The o(nlogn) solution involves sorting using merge sort and then finding the elements in o(n) worts case
#With o(1) constant extra memory
def divide(arr):
	if len(arr)==1:
		return arr
	mid = int(len(arr)/2)
	left = arr[0:mid]
	right = arr[mid:]
	return merge(divide(left),divide(right))
def merge(left,right):
	res = []
	left_index = 0
	right_index = 0
	while (left_index<len(left) and right_index<len(right)):
		if(left[left_index]<right[right_index]):
			res.append(left[left_index])
			left_index+=1
		else:
			res.append(right[right_index])
			right_index+=1
	return res+left[left_index:]+right[right_index:]
	
#Now let's solve the problem
def findTwo(coins,v):
	sort_ = divide(coins)
	l = 0
	r = len(coins)-1
	while (l<r):
		total = sort_[l]+sort_[r]
		if total==v:
			return sort_[l],sort_[r]
		elif total<v:
			l+=1
		else:
			r-=1
	return None


coins = [1,1,1,1,4]
v = 4
res = findTwo(coins,v)
if res:
	print(res)
else:
	print("There is no such pair in the array")


#Now look at recursive function which will return 
#True
print(recursion(coins,v,0))