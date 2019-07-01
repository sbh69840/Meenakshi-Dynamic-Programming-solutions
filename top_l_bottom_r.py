
def solve(n):
    count1 = [0]
    count = [0]
    dp = []
    for a in range(1000):
        dp.append([-1]*1000)
    def move(x,y):
        count1[0]+=1
        if dp[x][y]!=-1:
            count[0]+=1
            return dp[x][y]
        if x==y==(n-1):
            return 1
        if x>=n or y>=n:
            return 0
        ways = move(x+1,y)+move(x,y+1)
        dp[x][y] = ways
        return ways
    return move(0,0),count,count1
def solve_iter(n):
    arr = []
    for a in range(n):
        arr.append([0]*n)
    for b in range(n):
        if b!=(n-1):
            arr[-1][b] = 1
            arr[b][-1] = 1

    for a in range(n-1,-1,-1):
        for b in range(n-1,-1,-1):
            if b!=(n-1) and a!=(n-1):
                arr[a][b] = arr[a][b+1]+arr[a+1][b]
    return arr[0][0]
t = int(input("Test cases\n"))
for a in range(t):
    n = int(input("Enter the size of the matrix\n"))
    file = open("test.txt","w+")
    #file.write(str(solve_iter(n)))
    #file.close()
    print("The number of ways from 0,0 to n,n = ",len(str(solve(n))))
        
