
def recursion(coins,v,count):
	if v==0:
		return coins,True
	if len(coins)==0:
		return False
	if coins[0]>v:
		recursion(coins[1:],v,count)
	return recursion(coins[1:],v-coins[0],count+1) or recursion(coins[1:],v,count)

coins = [5,6,4,3,2,6,7]
v = 9

print(recursion(coins,v,0))