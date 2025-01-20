class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq_dict={}

        for i in arr:
            freq_dict[i]=freq_dict.get(i,0)+1

        return len(list(freq_dict.keys()))==len(set(freq_dict.values()))
        