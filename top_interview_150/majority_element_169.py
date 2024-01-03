class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        freq_dict={}
        for num in nums:
            freq_dict[num]=freq_dict.get(num,0)+1

        return [i for i,j in freq_dict.items() if j>n//2][0]
