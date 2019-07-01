#This gives a solution to finding the partition of 
#array such that both the parts have minimum difference of sum and print the maximum 
#sum out of the two sum's
import math
current_min = math.inf
current_max = 0
def solve(arr,index,sum_so_far,total_sum):
	if index==0:
		ans = abs((total_sum-sum_so_far)-sum_so_far)
		global current_min
		global current_max
		if ans<current_min:
			current_min = ans
			current_max = max((total_sum-sum_so_far),sum_so_far)
		return ans
	ans1 = min(solve(arr,index-1,sum_so_far+arr[index-1],total_sum),solve(arr,index-1,sum_so_far,total_sum))
	return ans1
solve([1,2,3,4],4,0,10)
print(current_max)
# current_max = 0
# current_min = math.inf 
# new_res = []
# for a in max_sum:
# 	if a[1]<current_min:
# 		current_min = a[1]
# for a in max_sum:
# 	if a[1]==current_min:
# 		new_res.append(a[0])
# print(max(new_res))