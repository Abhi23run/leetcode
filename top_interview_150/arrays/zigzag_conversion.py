class Solution:
    def convert(self, s: str, numRows: int) -> str:
        row_index = 1
        i = 0
        final_output = [[] for i in range(numRows)]
        while (i < len(s)):
            while ((row_index <= numRows) and (i < len(s))):
                final_output[row_index-1].append(s[i])
                row_index += 1
                i += 1
            row_index = max(numRows-1, 1)
            while ((row_index > 0) and (i < len(s))):
                final_output[row_index-1].append(s[i])
                row_index -= 1
                i += 1
            row_index = min(2, numRows)

        return ''.join([''.join(i) for i in final_output])
