class Solution:
    def maxArea(self, heights: List[int]) -> int:

        L = 0
        R = len(heights) - 1
        maxArea = 0
        while L < R:

            minHeight = min(heights[L], heights[R]) 
            diff = R - L
            area = minHeight * diff
            maxArea = max(maxArea, area)
            if heights[L] <=  heights[R]:
                L += 1
            elif heights[R] < heights[L]:
                R -= 1
        return maxArea           
        