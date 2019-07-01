def recursion(n):
    def solve1(n):
        if n<0:
            return 0
        if n==0:
            return 1
        return solve1(n-3)+solve1(n-5)+solve1(n-10)
    def solve(n):
        x = solve1(n-3)
        y = solve1(n-5)
        z = solve1(n-10)
        return x+y+z
    return solve(n)
n = int(input())
print("Recursion = ",recursion(n))

