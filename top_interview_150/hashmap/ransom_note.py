class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq_dict_big={}
        freq_dict_small={}
        for char in ransomNote:
            freq_dict_small[char]=freq_dict_small.get(char,0)+1
        for char in magazine:
            freq_dict_big[char]=freq_dict_big.get(char,0)+1

        for ele,count in freq_dict_small.items():
            if count>freq_dict_big.get(ele,0):
                return False
        return True
        
        


        