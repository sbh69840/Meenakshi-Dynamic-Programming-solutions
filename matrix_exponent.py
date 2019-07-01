def multiply(A,B):
    result = [[0 for _ in range(len(A))] for _ in range(len(A))]
    for a in range(len(A)):
        for b in range(len(A)):
            sum_ = 0
            for c in range(len(A)):
                sum_+=((A[a][c]*B[c][b])%1000000007)
            result[a][b] = sum_
    return result
def power(A,n):
    result = [[0 for _ in range(len(A))] for _ in range(len(A))]
    for i in range(len(A)):
        result[i][i]=1
    while n>0:
        if n%2==1:
            result = multiply(result,A)
        A = multiply(A,A)
        n = int(n/2)
    return result
def final(ini,A,n):
    ans = power(A,n-2)
    print(ans)
    result = 0
    for a in range(len(A)):
        result+=((ini[a]*ans[a][0])%1000000007)
    return result
def random(n):
    a = 1
    b=2
    c=4
    ans=4
    for i in range(4,n+1):
        ans = (a+b+c)%1000000007
        a = b
        b = c
        c = ans
    return ans
A = [[1,1,0],[1,0,1],[1,0,0]]
ini = [2,1,1]
n = int(input())
import time
start = time.time()
print(start)
print(final(ini,A,n)%1000000007)
print(time.time())
#start =time.time()
#print("Random result = ",random(n)," Time = ",time.time()-start)

        
