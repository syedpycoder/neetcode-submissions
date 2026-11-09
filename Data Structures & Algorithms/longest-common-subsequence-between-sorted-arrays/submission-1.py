class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:

        common = set(arrays[0])

        for element in arrays:
            common = common.intersection(element)

        return sorted(common)    
        

       