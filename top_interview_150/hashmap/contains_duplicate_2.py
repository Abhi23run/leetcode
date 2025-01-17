class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window=set()
        l=0
        for r in range(l,len(nums)):
            if r-l>k:
                window.remove(nums[l])
                l+=1
            if nums[r] in window:
                return True
            else:
                window.add(nums[r])

        return False

            
            







        