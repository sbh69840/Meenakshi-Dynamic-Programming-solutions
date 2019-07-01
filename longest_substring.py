num = input("Enter the string to find the longest substring with sum on the left equal to the sum on the right.")
def maxlen(str_):
    sum_ = []
    n = len(str_)
    for a in range(n):
        sum_.append([0]*n)
        sum_[a][a]=int(str_[a])
    maxlen_ = 0
    final = ""
    for a in range(2,n+1):
        for b in range(0,n-a+1):
            c = b+a-1
            k = int(a/2)
            sum_[b][c] = sum_[b][c-k]+sum_[c-k+1][c]
            if a%2==0 and sum_[b][c-k]==sum_[c-k+1][c] and a>maxlen_:
                maxlen_=a
                final = str_[b:c+1]
    return maxlen_,final
def bruteforce(str_):
    maxlen_ = 0
    n = len(str_)
    final = ""
    for a in range(0,n):
        for b in range(a+1,n,2):
            len_ = b-a+1
            k = int(len_/2)
            left = sum(list(map(int,str_[a:b-k+1])))
            right = sum(list(map(int,str_[b-k+1:b+1])))
            if left==right and len_>maxlen_:
                maxlen_=len_
                final = str_[a:b+1]
    return maxlen_,final
import time
start=time.time()
print(maxlen(num),"Time taken = ",time.time()-start)
start = time.time()
print(bruteforce(num),"Time taken = ",time.time()-start)

                
    
