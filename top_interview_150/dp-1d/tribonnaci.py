class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1
        else :
            tp=[0]*(n+1)
            tp[0],tp[1],tp[2]=0,1,1
            for i in range(3,n+1):
                tp[i]=tp[i-1]+tp[i-2]+tp[i-3]
        
            return tp[n]