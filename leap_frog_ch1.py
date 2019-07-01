
count_ = 0
def leap_frogs(arr):
	n = len(arr)
	dir = [False]*n
	perm = []
	left_to_right = True
	right_to_left = False
	count_b = arr.count(1)
	
	def Mobile(arr,dir,n):
		mob = 0
		prev_mob = 0
		for i in range(n):
			if (dir[arr[i]-1]==right_to_left and i!=0):
				if (arr[i]>arr[i-1] and arr[i]>prev_mob):
					mob = arr[i]
					prev_mob = mob 
			elif (dir[arr[i]-1]==left_to_right and i!=n-1):
				if (arr[i]>arr[i+1] and arr[i]>prev_mob):
					mob = arr[i]
					prev_mob = mob 
		if mob==0 and prev_mob ==0:
			return 0
		else:
			return mob 
	def swap(arr,i,j):
		tmp = arr[i]
		arr[i] = arr[j]
		arr[j] = tmp 
	def fact(n):
		res = 1
		for a in range(2,n+1):
			res*=a
		return res
	
	def johnson_trotter(arr,dir,n):
		
		mob = Mobile(arr,dir,n)
		
		try:
			ind = arr.index(mob)

			if (dir[arr[ind]-1]==left_to_right):
				swap(arr,ind,ind+1)
			elif (dir[arr[ind]-1]==right_to_left):
				swap(arr,ind,ind-1)
			print(" | ",arr," | ")
			if arr[0]==1 and arr[-1]==2:
				cont_dots = 0
				max_cont = 0
				for a in arr:
					if a==2:
						cont_dots+=1
					else:
						cont_dots = 0
					if cont_dots>max_cont:
						max_cont = cont_dots
				
				if max_cont>1:
					return False
				else:
					return True

			else:
				return False
		except:
			global count_
			count_+=1
		for i in range(n):
			if (arr[i]>mob):
				if(dir[arr[i]-1]==left_to_right):
					dir[arr[i]-1]=right_to_left
				elif(dir[arr[i]-1]==right_to_left):
					dir[arr[i]-1]=left_to_right
		

	c = n-count_b
	if c==0:
		c=1
	if count_b==0:
		count_b=1
	num = int(fact(n)/(count_b*(c)))
	print(num)
	
	final = False
	if arr[0]==1 and arr[-1]==2:
			cont_dots = 0
			max_cont = 0
			for a in range(n):
				if a==2:
					cont_dots+=1
				else:
					cont_dots = 0
				if cont_dots>max_cont:
					max_cont = cont_dots
			print(max_cont)
			if max_cont>1:
				final =  False
			else:
				final =  True
	
	for i in range(1,num):
		res = johnson_trotter(arr,dir,n)
		final = final or res
		if final==True:
			break
	print(count_)
	for i in range(count_+1):
		res = johnson_trotter(arr,dir,n)
		final = final or res
		if final==True:
			break
	return final

def convert(arr):
	new_arr = []
	for a in arr:
		if a=="A":
			pass
		elif a=="B":
			new_arr.append(1)
		else:
			new_arr.append(2)
	return new_arr

t = int(input())
for a in range(1,t+1):
	count_=0
	inp = input()
	arr = convert(inp)
	if leap_frogs(arr):
		print("Case #",a,": Y")
	else:
		print("Case #",a,": N")



