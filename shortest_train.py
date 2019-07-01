import time
def train(mat):
    dp = []
    for a in range(100):
        dp.append([-2]*100)
    def min_cost(source,dest):
        if dp[source][dest]!=-2:
            print("he haaa")
            return dp[source][dest]
        lowest = mat[source][dest]
        if source==dest or source==(dest-1):
            return mat[source][dest]
        for i in range(source+1,dest):
            tmp = min_cost(source,i)+min_cost(i,dest)
            if tmp<lowest:
                lowest = tmp
                dp[source][dest] = lowest
        return lowest
    return min_cost(0,len(mat[0])-1)
n = int(input("Enter the size of the matrix\n"))
mat = []
for i in range(n):
    mat.append(list(map(int,input("Enter all n values of the row.\n").split(" "))))
start = time.time()
lowest = train(mat)
print("Minimum cost to travel from station 1 to n is = ",lowest,time.time()-start)
