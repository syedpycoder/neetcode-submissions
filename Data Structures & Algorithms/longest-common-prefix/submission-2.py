class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:


        min_string = min(strs, key = len)
        prefix = ''

        for pos, ch in enumerate(min_string):
            c = 0
            for element in strs:
                if element[pos] == ch:
                    c += 1
                else:
                    break
            if c == len(strs):
                prefix += ch
            else:
                break
        return prefix            



       