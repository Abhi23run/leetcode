class Solution:
    def isAnagram(self,s:str,t:str):
        freq_dict_s={}
        freq_dict_t={}

        for char in s:
            freq_dict_s[char]=freq_dict_s.get(char,0)+1
        for char in t:
            freq_dict_t[char]=freq_dict_t.get(char,0)+1

        return freq_dict_s==freq_dict_t

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n=len(strs)
        unique_set=set()
        output_list=[]
        for i in range(n):
            if strs[i] in unique_set:
                continue
            else:
                unique_set.add(strs[i])
                sublist=[strs[i]]
                j=i+1
                while(j<n):
                    if self.isAnagram(strs[i],strs[j]):
                        sublist.append(strs[j])
                        unique_set.add(strs[j])
                    j+=1
                output_list.append(sublist)

        return output_list