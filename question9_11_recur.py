#Not the correct answer. Maybe one day I will be able to solve it.
def lis_recur(arr,index,subarr):
	if index==len(arr):
		return len(subarr)
	else:
		if len(subarr)>0:
			if arr[index]>subarr[-1]:
				first = lis_recur(arr,index+1,subarr)
				second = lis_recur(arr,index+1,subarr+[arr[index]])
			else:
				first = lis_recur(arr,index+1,subarr)
				second = 0
		else:
			first = lis_recur(arr,index+1,subarr)
			second = lis_recur(arr,index+1,subarr+[arr[index]])
	mi = max(first,second)
	global maximum_lis
	if mi>maximum_lis[index]:
		maximum_lis[index] = mi 
		global lis_subarr
		lis_subarr[index] = subarr
	return max(first,second)
def lds_recur(arr,index,subarr):
	if index==len(arr):
		return len(subarr)
	else:
		if len(subarr)>0:
			if arr[index]<subarr[-1]:
				first =lds_recur(arr,index+1,subarr)
				second = lds_recur(arr,index+1,subarr+[arr[index]])
			else:
				first = lds_recur(arr,index+1,subarr)
				second = 0
		else:
			first = lds_recur(arr,index+1,subarr)
			second = lds_recur(arr,index+1,subarr+[arr[index]])
	mi = max(first,second)
	global maximum_lds
	if mi>maximum_lds[index]:
		maximum_lds[index] = mi 
		global lds_subarr
		lds_subarr[index] = subarr
	return max(first,second)
arr = [1,11,2,10,4,5,2,1]
lis_subarr = [[] for _ in range(len(arr))]
lds_subarr = [[] for _ in range(len(arr))]
maximum_lis = [0 for _ in range(len(arr))]
maximum_lds = [0 for _ in range(len(arr))]
print("LIS max length = ",(lis_recur(arr,0,[])))
print("LIS subarray's at index i = ",lis_subarr)
print("LDS max length = ",(lds_recur(arr,0,[])))
#We reverse it because we want the longest decreasing sequence from the end to that index in lds_subarr
lds_subarr = [lds_subarr[i] for i in range(len(lds_subarr)-1,-1,-1)]
print("LDS subarray's at index i = ",lds_subarr)
max_lbs = 0
lbs_subarr = []
for i in range(len(arr)):
	if (len(lis_subarr[i])+len(lds_subarr[i])-1)>max_lbs:
		max_lbs = (len(lis_subarr[i])+len(lds_subarr[i])-1)
		lbs_subarr = lis_subarr[i]+lds_subarr[i]
print("LBS max length = ",max_lbs)
print("LBS max_subarray = ",lbs_subarr)