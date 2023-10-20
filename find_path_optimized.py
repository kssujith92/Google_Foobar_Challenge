def solution(M):
    def min_len(M,H,W,C):
        
        Q=[(H-1,W-1,1000,1)]
        XY=(H-1)*W+W-1
        D={XY:[(1000,0)]}
   
        while Q:
            print(Q)
            q=Q.pop()
            x,y,pxy,c=q[0],q[1],q[2],q[3]
            xy=x*W+y
            print('Current Step: ',q)
            print('C=',C,'c=',c)
            if c>=C:
                continue
            for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                nx,ny=x+dx,y+dy
                print(nx,ny,c)
                nxy=nx*W+ny
                if 0<=nx<H and 0<=ny<W and pxy!=nxy:
                    if (nx,ny)==(0,0):
                        if c+1<C: 
                            C=c+1
                        print('Target reached. c=',c+1)
                    elif M[nx][ny]==0:
                        if nxy in D:
                            if (xy,1) in D[nxy]:
                                    continue
                        else:
                            D[nxy]=[]
                        Q.append((nx,ny,xy,c+1))
                        D[nxy].append((xy,0))
            Q.sort()
            D[xy].append((pxy,1))
        return C
    
    H=len(M)
    W=len(M[0])
    l= min_len(M,H,W,H*W)
    
    
    for i in range(H):
        for j in range(W):
            if M[i][j]==1:
                print(i,j)
                Mt=list(M)
                Mt[i][j]=0
                lt=min_len(Mt,H,W,l)
                if l>lt: l=lt
    return l

print(solution([[0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0], 
                [0, 1, 1, 1, 1, 1, 1], 
                [0, 0, 0, 0, 0, 0, 0], 
                [1, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 1], 
                [0, 0, 0, 0, 0, 0, 0]]))

#print(solution([[0, 0, 0, 0, 0, 0], 
 #               [1, 1, 1, 1, 1, 0], 
  #              [0, 0, 0, 0, 0, 0], 
   #             [0, 1, 1, 1, 1, 1], 
    #            [0, 1, 1, 1, 1, 1], 
     #           [0, 0, 0, 0, 0, 0]])) 
   
#print(solution([[0,0,0,0],
 #               [1,1,1,0],
  #              [1,0,0,0],
   #             [1,0,0,0]]))

#import numpy.random as r
#import time
#t=time.time()
#M=r.randint(0,1,size=(10,10))
#print(M)
#print(solution(M))
#print('Elapsed time =',time.time()-t)

    