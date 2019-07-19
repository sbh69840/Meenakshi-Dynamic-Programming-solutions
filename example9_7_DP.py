#When you look at the bactrack code in example9_7.py file you will see
#that it's pretty much intutive to convert it to DP.
#When you look at it you might think that the for loop that 
#runs for len(coins)+1 times will be the first foor loop in the DP approach
#,but you are wrong. Imagine what happens in two for loops, the first for loop
#has a fixed value and the second for loop keeps moving, similarly when you call 
#coins_backtrack function, that remains fixed and the len(coins) keeps changing, which is
#not the exact reason but, that gives he intution as to why the sum has to be the outer for loop
import random
coins = [random.randint(1,20) for _ in range(5)]
req_num = random.randint(1,100)
print(coins,req_num)
DP = [math.inf]*len(coins)+1
DP[0]=0
for i in range(req_sum):
	for j in range(len(coins)):
		if coins[j]<=i:
			temp = DP[i-coins[j]]
			if temp+1<DP[i]:
				DP[i]=temp+1
print(DP[len(coins)])
