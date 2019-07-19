#This is the recursive approach I am trying before I looked at the approach given in the book
#O(3^n) is the time complexity
#This is better than backtrack approach which has worst case time complexity
#of  O(required_sum^n), which reduces once memoized. Next I will be comparing the time for both
#on a larger array in a IPYNB. Since I am also printing the min_coins array in recursive 
#code this will take more time becuase of the auxillary space allocation and append time 
#which are in addition to the time taken to find the sum.

#Apparently both my codes are flawed minCoins and minCoinsNA
#They work totally fine when repetitions of coins are not allowed, but when it comes to 
#repetition, we don't really know how many times to repeat to give the exact minimum
#And hence my approach as of now is flawed.
import math
def minCoins(coins,required_sum,index,coins_chosen):
	if required_sum==0:
		print(coins_chosen)
		return len(coins_chosen)
	elif index==len(coins):
		return math.inf 
	else:
		first = minCoins(coins,required_sum-coins[index],index+1,coins_chosen+[coins[index]])
		second = minCoins(coins,required_sum,index+1,coins_chosen)
		if coins[index]!=1:
			third = minCoins(coins,required_sum-(coins[index]*math.floor(required_sum/coins[index])),index+1,coins_chosen+[\
				coins[index]]*math.floor(required_sum/coins[index]))
		else:
			third = minCoins(coins,required_sum-(required_sum),index+1,coins_chosen+[1]*required_sum)
		return min(first,second,third)
coins = [1,2,3]
req_sum = 7
print(minCoins(coins,req_sum,0,[]))
def minCoinsNA(coins,required_sum,index):
	if required_sum==0:
		return 1
	elif index==len(coins):
		return math.inf
	else:
		first = minCoinsNA(coins,required_sum,index+1)
		second = minCoinsNA(coins,required_sum-coins[index],index+1)
		third = minCoinsNA(coins,required_sum-(coins[index]*math.floor(required_sum/coins[index])),index+1)
		return min(first,second,third+math.floor(required_sum/coins[index]))
print(minCoinsNA(coins,req_sum,0))
#Backtrack approach given in the book.
class Memo:
	def __init__(self,fn):
		self.fn = fn
		self.memory = {}
	def __call__(self,*args):
		if args[1] not in self.memory:
			self.memory[args[1]]=self.fn(*args)
		return self.memory[args[1]]
@Memo 
def coins_backtrack(arr,current_sum):
	if current_sum==0:
		return 0
	else:
		res = math.inf
		for i in range(len(arr)):
			if arr[i]<=current_sum:
				temp = coins_backtrack(arr,current_sum-arr[i])
				if temp+1<res:
					res = temp+1
		return res
print(coins_backtrack(coins,req_sum)) 