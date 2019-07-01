n = int(input())
def recursion(n):
    def solve1(n):
        if n==1:
            return 1
        if n==0:
            return 0
        return solve(n-1)+solve1(n-2)
    def solve(n):
        if n==0:
            return 1
        if n==1:
            return 0
        
        return solve(n-2)+(2*solve1(n-1))
    return solve(n)
print(recursion(n))
