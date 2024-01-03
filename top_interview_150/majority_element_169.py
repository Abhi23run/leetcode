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


### Interesting Approach: Sorting 
## The intuition behind this approach is that if an element occurs more than n/2 times in the array (where n is the size of the array), it will always occupy the middle position when the array is sorted. Therefore, we can sort the array and return the element at index n/2.

## Final Approach : Moore's Voting Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        ##Moore's Voting Algorithm
        count = 0
        candidate = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate
