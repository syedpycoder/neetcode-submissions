class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:

        min_value = arrays[0][0]
        max_value = arrays[0][-1]
        result = float('-inf')


        n = len(arrays)

        for i in range(1, n):
            result = max(result, max(abs(max_value - arrays[i][0]), abs(arrays[i][-1] - min_value)))
            max_value = max(max_value, arrays[i][-1])
            min_value = min(min_value, arrays[i][0])

        return result    

       