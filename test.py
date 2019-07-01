class cell:
	def __init__(self,x,y,move):
		self.x = x
		self.y = y
		self.move = move
def isInside(x,y,N):
	if x>=0 and x<N and y>=0 and y<N:
		return True
	return False
def solve(source,dest,N):
	queue = []
	queue.append(cell(source[0],source[1],0))
	visited = [[False for _ in range(N)] for _ in range(N)]
	visited[source[0]][source[1]] = True
	xmoves = [1,2,2,1,-2,-1,-1,-2]
	ymoves = [2,1,-1,-2,-1,-2,2,1]
	while len(queue)>0:
		t = queue[0]
		queue.pop(0)
		if t.x==dest[0] and t.y==dest[1]:
			return t.move 
		for a in range(len(xmoves)):
			x = t.x + xmoves[a]
			y = t.y + ymoves[a]
			if isInside(x,y,N) and not visited[x][y]:
				visited[x][y]=True
				queue.append(cell(x,y,t.move+1))
print(solve([0,0],[29,29],30))