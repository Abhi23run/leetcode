class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        max_length=float("-inf")
        unique_set=set()

        for r in range(len(s)):  
            if s[r] not in unique_set:   
                max_length=max(max_length,r-l+1)
            else:
                while(s[r] in unique_set):
                    unique_set.remove(s[l])
                    l+=1
            unique_set.add(s[r]) 

        return 0 if max_length==float("-inf") else max_length



            
        
        