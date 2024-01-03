class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        ##Time Complexity: O(n), Space Complexity: O(n)
        n=len(nums)
        freq_dict={}
        for num in nums:
            freq_dict[num]=freq_dict.get(num,0)+1

        return [i for i,j in freq_dict.items() if j>n//2][0]


### Improved Solution as existence of a majority solutions is guaranteed
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        ##Time Complexity: O(n), Space Complexity: O(1) 
        n=len(nums)
        freq_dict={}
        for num in nums:
            freq_dict[num]=freq_dict.get(num,0)+1
            if freq_dict[num]>n//2:
                return num 
