def solution(h, q):
    
    def lsplit(el,l,t):
        N=(2**l)-1;
        print('N=',N,'el=',el);
        if el==N:
          print('Yay')
          return t;
        elif el<=N/2:
          print('Left');
          print('N=',N,'el=',el);
          return lsplit(el,l-1,N);
        else:
          print('Right');
          n=2**(l-1)-1;
          return n+lsplit(el-n,l-1,N-n);
            
            
    l=h;t=-1;
    p=[];
    for el in q:
        p.append(lsplit(el,l,t));
        print('Solution found',p)
    return p;
    
print(solution(3, [7, 3, 5, 1]));