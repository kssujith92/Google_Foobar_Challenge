def solution(n):
    def solvebricks(b,p,D):
        d=b*1000+p #unique key for (b,p)
        if d in D:
            return D[d]
        elif b==0:
            return 1
        elif p<=1:
            return 0
        else:
            c=0
            for i in range(b,0,-1):
                if i<p:
                    j=b-i #remaining bricks
                    c+=solvebricks(j,i,D)
            D[d]=c
            return c
                
    b=n #no. of bricks
    D={}
    c=solvebricks(n,b,D)
    return c