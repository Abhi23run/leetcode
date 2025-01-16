class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_dict_s={}
        freq_dict_t={}

        for char in s:
            freq_dict_s[char]=freq_dict_s.get(char,0)+1
        for char in t:
            freq_dict_t[char]=freq_dict_t.get(char,0)+1

        return freq_dict_s==freq_dict_t