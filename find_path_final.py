def solution(M):
    
    def distance(M):
        #distance to every node from the start
        d=[[1 if i==j==0 else 500 for j in range(W)] for i in range(H)]

        Q=[(0, 0)]
        while Q:
            x,y=Q.pop(0)
            for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                nx,ny=x+dx,y+dy
                if 0<=nx<H and 0<=ny<W:
                    if d[nx][ny]==500:
                        d[nx][ny]=d[x][y]+1
                        if M[nx][ny]==0:
                            Q.append((nx,ny))
        return d
    
    def flip(M):
        return [[e for e in reversed(r)] for r in reversed(M)]
    
    H=len(M)
    W=len(M[0])
    D = distance(M)                 #distances from start
    DF = flip(distance(flip(M)))    #distances from end
    # find shortest path: add and min
    return min([sum(s)-1 for i in range(H) for s in zip(D[i],DF[i])])

print(solution([[0, 0, 0, 0, 0, 0], 
                [1, 1, 0, 1, 1, 0], 
                [0, 0, 0, 0, 0, 0], 
                [0, 1, 1, 1, 1, 1], 
                [0, 1, 1, 1, 1, 1], 
                [0, 0, 0, 0, 0, 0]]))
           
