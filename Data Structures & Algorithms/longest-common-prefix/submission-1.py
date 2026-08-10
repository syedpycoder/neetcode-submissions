class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        min_str = min(strs, key = len)
        common_prefix = ''

        for pos, ch in enumerate(min_str):
            c = 0
            for element in strs:
                if element[pos] == ch:
                    c += 1
                else:
                    break
            if c == len(strs):
                common_prefix += ch
            else:
                break
        return common_prefix                        

