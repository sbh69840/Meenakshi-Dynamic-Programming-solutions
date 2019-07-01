t = int(input())
for a in range(t):
    n,p = map(int,input().split())
    a = list(map(int,input().split()))
    min_ = []
    for ind,b in enumerate(a):
        min_.append((b^((n-ind)))&b)
    print(min_)
    minimum = abs(min_[0]-p)
    for b in min_:
        if abs(b-p)<minimum:
            minimum = abs(b-p)
    for b in a:
        if abs(b-p)<minimum:
            minimum=abs(b-p)
    print(minimum)
