class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp={} # stores number of ways of attaining the total using all elements till index i dp[(i,total)]
        def helper_fn(index,total):
            if (index==len(nums)):
                return 1 if total==target else 0
            if (index,total) in dp:
                return dp[(index,total)]

            dp[(index,total)]=helper_fn(index+1,total-nums[index])+helper_fn(index+1,total+nums[index])

            return dp[(index,total)]

        return helper_fn(0,0)
