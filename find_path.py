#Find shortest path from bottom right to top left in a matrix. 0 is way, 1 is wall. 
#Only left,right,up,down movements.
#Change one of the walls to make it shorter if possible.


def solution(M):
    def moveleft(M,h,w,D,d):
        f=0
        if M[h][w-1]==0:
            D[d].extend([1+i for i in findlen(M,h,w-1,h,w,D)])
            f=1
        return D,f
        
    def moveright(M,h,w,D,d):
        f=0
        if M[h][w+1]==0:
            D[d].extend([1+i for i in findlen(M,h,w+1,h,w,D)])
            f=1
        return D,f
        
    def moveup(M,h,w,D,d):
        f=0
        if M[h-1][w]==0:
            D[d].extend([1+i for i in findlen(M,h-1,w,h,w,D)])
            f=1
        return D,f
    def movedown(M,h,w,D,d):
        f=0
        if M[h+1][w]==0:
            D[d].extend([1+i for i in findlen(M,h+1,w,h,w,D)])
            f=1
        return D,f
    
    def findlen(M,h,w,hp,wp,D):
        d=h*100+w
        H=len(M)-1
        W=len(M[0])-1
        f=[0,0,0,0,0]
        
        if d in D:
            f[0]=1
            return D[d]
        else:
            D[d]=[]
            if h==0 and w==0:
                f[0]=1
                return [1]
            elif h>0 and h<H:
                if w>0 and w<W:
                    if wp!=w-1: D,f[1]=moveleft(M,h,w,D,d)
                    if wp!=w+1: D,f[2]=moveright(M,h,w,D,d)
                    if hp!=h-1: D,f[3]=moveup(M,h,w,D,d)
                    if hp!=h+1: D,f[4]=movedown(M,h,w,D,d)
                elif w==W:
                    if wp!=w-1: D,f[1]=moveleft(M,h,w,D,d)
                    if hp!=h-1: D,f[2]=moveup(M,h,w,D,d)
                    if hp!=h+1: D,f[3]=movedown(M,h,w,D,d)
                elif w==0:
                    if wp!=w+1: D,f[1]=moveright(M,h,w,D,d)
                    if hp!=h-1: D,f[2]=moveup(M,h,w,D,d)
                    if hp!=h+1: D,f[3]=movedown(M,h,w,D,d)
            elif h==H:
                if w>0 and w<W:
                    if wp!=w-1: D,f[1]=moveleft(M,h,w,D,d)
                    if wp!=w+1: D,f[2]=moveright(M,h,w,D,d)
                    if hp!=h-1: D,f[3]=moveup(M,h,w,D,d)
                elif w==W:
                    if wp!=w-1: D,f[1]=moveleft(M,h,w,D,d)
                    if hp!=h-1: D,f[3]=moveup(M,h,w,D,d)
                elif w==0:
                    if wp!=w+1: D,f[2]=moveright(M,h,w,D,d)
                    if hp!=h-1: D,f[3]=moveup(M,h,w,D,d)
            elif h==0:
                if w>0 and w<W:
                    if wp!=w-1: D,f[1]=moveleft(M,h,w,D,d)
                    if wp!=w+1: D,f[2]=moveright(M,h,w,D,d)
                    if hp!=h+1: D,f[4]=movedown(M,h,w,D,d)
                elif w==W:
                    if wp!=w-1: D,f[1]=moveleft(M,h,w,D,d)
                    if hp!=h+1: D,f[3]=movedown(M,h,w,D,d)
                elif w==0:
                    if wp!=w+1: D,f[2]=moveright(M,h,w,D,d)
                    if hp!=h+1: D,f[3]=movedown(M,h,w,D,d)
            if sum(f)==0:
                return [500]
        return D[d]
    
    
    H=len(M)-1
    W=len(M[0])-1
    D={}
    L=findlen(M,H,W,H,W,D)
    l=min(L)
    print(L)
    print('Shortest = ',l)
    for i in range(H-1,0,-1):
        for j in range(W-1,0,-1):
            if M[i][j]==1:
                Mt=M
                Mt[i][j]=0
                L=findlen(Mt,H,W,H,W,{})
                if l>min(L): l=min(L)
    return l

import numpy.random as r
import time

M=r.randint(0,1,(10,10))

tic=time.time()
print(solution(M))
print('Elapsed time =',time.time()-tic)