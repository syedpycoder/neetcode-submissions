class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:

        min_val = arrays[0][0]
        max_val = arrays[0][-1]

        n = len(arrays)
        res = float('-inf')
        
        for i in range(1, n):
            diff1 = abs(max_val-arrays[i][0])
            diff2 = abs(arrays[i][-1] - min_val)
            res = max(res, max(diff1, diff2))
            max_val = max(max_val, arrays[i][-1])
            min_val = min(min_val, arrays[i][0])

        return res    



      