class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #O(nlogn solution)
        l,r,total=0,0,0
        min_length=float("inf")
        while(r<len(nums)):
            total+=nums[r]
            while total>=target:
                min_length=min(r-l+1,min_length)
                total-=nums[l]
                l+=1
            
            r+=1
        if min_length==float("inf"):
            return 0
        else:
            return min_length



        