class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_t_map={}
        t_s_map={}
        for ele_s,ele_t in zip(s,t):
            if ele_s in s_t_map:
                if s_t_map[ele_s]!=ele_t:
                    return False
            else:
                s_t_map[ele_s]=ele_t

        for ele_t,ele_s in zip(t,s):
            if ele_t in t_s_map:
                if t_s_map[ele_t]!=ele_s:
                    return False
            else:
                t_s_map[ele_t]=ele_s
        
        return True