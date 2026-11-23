class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        count = 0
        expected = sorted(heights)

        for val1, val2 in zip(heights, expected):
            if val1 != val2:
                count += 1

        return count        
        