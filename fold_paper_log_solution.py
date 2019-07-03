import math
h,w,h1,w1 = map(int,input().split())
res = 0
if h1!=1:
	res+=math.floor(math.log10((h/h1))/math.log10(2))+1
	#If you observe the sequence of folding papers of h1 or w1 > 1, it will be as follows (consider n = 3):
	#h = 3 h1 = 3 => 0
	#h = 4 h1 = 3 => 1
	#h = 5 h1 = 3 => 1
	#h = 6 h1 = 3 => 1
	#h = 7 h1 = 3 => 2
	#h = 8 h1 = 3 => 2
	#h = 9 h1 = 3 => 2
	#h = 10 h1 = 3 => 2
	#h = 11 h1 = 3 => 2
	#h = 12 h1 = 3 => 2
	#h = 13 h1 = 3 => 3
	#h = 14 h1 = 3 => 3
	#h = 15 h1 = 3 => 3
	#h = 16 h1 = 3 => 3
	#h = 17 h1 = 3 => 3
	#h = 18 h1 = 3 => 3
	#h = 19 h1 = 3 => 3
	#h = 20 h1 = 3 => 3
	#h = 21 h1 = 3 => 3
	#h = 22 h1 = 3 => 3
	#h = 23 h1 = 3 => 3
	#h = 24 h1 = 3 => 3
	#h = 25 h1 = 3 => 4 
	#Observe the pattern and you will find the relation.
else:
	res+=math.ceil((math.log10(h)/math.log10(2)))
	#Let's now look at the pattern for h1 = 1:
	#h = 1 h1 = 1 => 0
	#h = 2 h1 = 1 => 1
	#h = 3 h1 = 1 => 2
	#h = 4 h1 = 1 => 2
	#h = 5 h1 = 1 => 3
	#h = 6 h1 = 1 => 3
	#h = 7 h1 = 1 => 3
	#h = 8 h1 = 1 => 3
	#h = 9 h1 = 1 => 4
	#I think so much evidence should suffice the argument.
#Now repeat the same process for width, because what rule applies for height, applies to width as well
if w1!=1:
	res+=math.floor(math.log10((w/w1))/math.log10(2))+1
else:
	res+=math.ceil((math.log10(w)/math.log10(2)))
print(res)

#Interesting fact about log base 2:
# i) To obtain a uniformly random distribution of n-deck card shuffle it (3*(logn))/2 times (riffle shuffle)
# ii) In music theory to calculate how many octaves (2:1 ratio) two different tones are, log(f1/f2) base 2 is used. 