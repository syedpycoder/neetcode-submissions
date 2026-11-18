class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        minStr = min(strs, key = len)
        commonPrefix = ''

        for pos, ch in enumerate(minStr):
            countElement = 0
            for element in strs:
                if element[pos] == ch:
                    countElement += 1
                else:
                    break    

            if countElement == len(strs):
                commonPrefix += ch
            else:
                break
        return commonPrefix            


       