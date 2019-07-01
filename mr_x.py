import sys
def valid(exp):
	open_ = ["("]
	close_ = [")"]
	expressions = ["X","x","0","1",""]
	val_exp= []
	operators = ["|","&","^"]
	def isvalid(exp):
		exp1 = '%s'%exp
		for a in val_exp:
			exp1 = exp1.replace(a,"x")
		if exp1 in expressions:
			return True
		if len(exp1)==3:
			if (exp1[0] in expressions) and (exp1[1] in operators) and (exp1[2] in expressions):
				return True
		return False

	def check(exp):
		stack = []
		is_operator = False
		ever_appended = False
		if exp in expressions:
			return True
		if exp[0] in operators:
			is_operator = True
		for i in range(len(exp)):


			if exp[i] in open_:
				ever_appended = True
				stack.append(i)

			elif exp[i] in close_:

				pos = close_.index(exp[i])
				if len(stack)>0:
					first = stack[len(stack)-1]

				if len(stack)>0 and open_[pos]==exp[first]:
					if(not isvalid(exp[first+1:i])):
						return False
					else:
						val_exp.insert(0,exp[first:i+1])
					stack.pop()
				else:
					return False
		if len(stack)==0 and not is_operator and ever_appended:
			return True
	return check(exp)
changes = ["|","&","^","X","x","0","1"]
step = []

def first_exp(exp):
	operators = ["|","&","^"]
	start = 0
	end = 0
	for ind,i in enumerate(exp):
		if i=="(":
			start=ind
		if i in operators:
			end = ind
			break
	return [start+1,end]


def check_same(exp):
	x = 1
	X = ~x
	res = eval(exp)
	x = 0
	X = ~x
	res1 = eval(exp)
	if res==res1:
		return True
	return False
def change_expression(exp,steps):
	res = check_same(exp)
	if res:
		return steps 

	for i in range(len(exp)):
		for j in changes:
			tmp = exp[i]
			exp = exp[:i]+j+exp[i+1:]
			if (valid(exp)):
				ans = check_same(exp)
			else:
				ans=False
			if ans:
				return 1
			exp= exp[:i]+tmp+exp[i+1:]
			
	#check for 2
	first_ = first_exp(exp)
	for i in range(first_[0],first_[1]+1):
		for j in range(i+1,first_[1]+1):
			for k in changes:
				tmp = exp[i]
				tmp1 = exp[j]
				exp = exp[:i]+k+exp[i+1:]
				exp = exp[:j]+k+exp[j+1:]
				if (valid(exp)):
					ans = check_same(exp)
				else:
					ans=False
				if ans:
					return 2
				exp = exp[:i]+tmp+exp[i+1:]
				exp = exp[:j]+tmp1+exp[j+1:]


# exp = "x^0"
# print(valid(exp))
# asd=asd
sys.stdin = open("mr_x.txt","r")
sys.stdout = open("output1.txt","w")
t = int(input().strip())
for a in range(1,t+1):
	exp = input().strip()
	ans = change_expression(exp,0)
	print("Case #"+str(a)+": "+str(ans))



