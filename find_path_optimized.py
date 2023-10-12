def solution(M):
    def min_len(M,H,W):
        
        Q=[(H-1,W-1,1)]
        D=[] 
        C=[]
   
        while Q:
            print(Q)
            q=Q.pop()
            x,y,c=q[0],q[1],q[2]
            print('Current Step: ',q)
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx,ny=x+dx,y+dy
                print(nx,ny,c)
                if 0<=nx<H and 0<=ny<W:
                    if (nx,ny)==(0,0):
                        C.append(c+1)
                        print('Target reached. c=',c+1)
                    elif M[nx][ny]==0:
                        if nx*W+ny in D:
                            print('Visited')
                            continue
                        Q.append((nx,ny,c+1))
            D.append(x*W+y)
            #print(D)
        print(C)
        return min(C)
    
    H=len(M)
    W=len(M[0])
    #l=500
    return min_len(M, H, W)
    
    
#    for i in range(H):
 #       for j in range(W):
  #          if Map[i][j]==1:
   #             print(i,j)
    #            Mt=list(Map)
     #           Mt[i][j]=0
      #          lt=min_len(Mt,H,W)
       #         if l>lt: l=lt
   # return l

print(solution([[0, 0, 0, 0, 0, 0], 
                [1, 1, 0, 1, 1, 0], 
                [0, 0, 0, 0, 0, 0], 
                [0, 1, 1, 1, 1, 1], 
                [0, 1, 1, 1, 1, 1], 
                [0, 0, 0, 0, 0, 0]]))
           