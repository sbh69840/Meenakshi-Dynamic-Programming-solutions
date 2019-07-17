
def lis_recur(arr,index,subarr):
	if index==len(arr):
		if len(subarr)>len(lis_subarr[index-1]):
			lis_subarr[index-1]=subarr
		return len(subarr)
	else:
		if len(subarr)>0:
			if arr[index]>subarr[-1]:
				first = lis_recur(arr,index+1,\
					subarr)
				second = lis_recur(arr,index+1,\
					subarr+[arr[index]])
			else:
				first = lis_recur(arr,index+1,\
					subarr)
				second = 0
			if len(subarr)>len(lis_subarr[index-1]):
				lis_subarr[index-1]=subarr
		else:
			first = lis_recur(arr,index+1,subarr)
			second = lis_recur(arr,index+1,\
				subarr+[arr[index]])
	return max(first,second)

arr = [1,11,2,10,4,5,2,1]
lis_subarr = [[] for _ in range(len(arr))]
lis_subarr[0].append(arr[0])
print("LIS max length = ",(lis_recur(arr,0,[])))
lis_subarr_final = lis_subarr.copy()
arr = list(reversed(arr))
lis_subarr = [[] for _ in range(len(arr))]
lis_subarr[0].append(arr[0])
print("LDS max length = ",lis_recur(arr,0,[]))
lds_subarr_final = lis_subarr.copy()
lds_subarr_final = [list(reversed(a)) for a in \
list(reversed(lds_subarr_final))]
print(lis_subarr_final)
print(lds_subarr_final)
max_lbs = 0
lbs = []
for i in range(len(arr)):
	len1 = len(lis_subarr_final[i])
	len2 = len(lds_subarr_final[i])
	if len1+len2-1>max_lbs:
		max_lbs = len1+len2-1 
	
print("MAX LBS length = ",max_lbs)
for i in range(len(arr)):
	len1 = len(lis_subarr_final[i])
	len2 = len(lds_subarr_final[i])
	if len1+len2-1==max_lbs:
		lbs.append(lis_subarr_final[i]+\
			lds_subarr_final[i][1:]) 
print("All LBS = ",lbs)