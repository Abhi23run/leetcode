class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_int_mapping={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500, 'M':1000}
        integer_val=symbol_int_mapping[s[0]]

        for i in range(1,len(s)):
            if symbol_int_mapping[s[i]]<=symbol_int_mapping[s[i-1]]:
                integer_val+=symbol_int_mapping[s[i]]
            else:
                integer_val-=symbol_int_mapping[s[i-1]]
                integer_val+=symbol_int_mapping[s[i]]-symbol_int_mapping[s[i-1]]
        return  integer_val