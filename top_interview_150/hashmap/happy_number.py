class Solution:
    def squaredigits(self,n :int)->int:
        count=0
        while n: 
            digit=n%10
            count+=digit**2
            n=n//10

        return count
    def isHappy(self, n: int) -> bool:
        visit=set()

        while n not in visit:
            visit.add(n)
            n=self.squaredigits(n)
            if n==1:
                return True
        return False



        