arr = [1,11,2,10,4,5,2,1]
LIS = [[] for _ in range(len(arr))]
LDS = [[] for _ in range(len(arr))]
LIS[0].append(arr[0])
for i in range(1,len(arr)):
	for j in range(0,i):
		if arr[j]<arr[i] and len(LIS[j])>len(LIS[i]):
			LIS[i]=LIS[j].copy()
	LIS[i].append(arr[i])
	if len(LIS[i])<len(LIS[i-1]):
		LIS[i]=LIS[i-1]
print(arr)
arr = [arr[i] for i in range(len(arr)-1,-1,-1)]
LDS[0].append(arr[0])
for i in range(1,len(arr)):
	for j in range(0,i):
		if arr[j]<arr[i] and len(LDS[j])>len(LDS[i]):
			LDS[i]=LDS[j].copy()
	LDS[i].append(arr[i])
	if len(LDS[i])<len(LDS[i-1]):
		LDS[i]=LDS[i-1]
#Reverse LDS to get the decreasing sequence from 
#index i (ranging from 0 to n-1)
LDS = [list(reversed(LDS[a])) for a in range(len(LDS)-1,-1,-1)]
max_lbs = 0
LBS = []
for i in range(len(arr)):
	if (len(LIS[i])+len(LDS[i])-1)>max_lbs:
		max_lbs = len(LIS[i])+len(LDS[i])-1
for i in range(len(arr)):
	if max_lbs==(len(LIS[i])+len(LDS[i])-1):
		LBS.append(LIS[i]+LDS[i][1:])
print(LIS)
print(LDS)
print("Max LBS length = ",max_lbs)
print("LBS = ",LBS)