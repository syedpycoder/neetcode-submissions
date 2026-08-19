class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        maxArea = 0
        stack = []

        for pos, height in enumerate(heights):
            start = pos
            while stack and stack[-1][1] > height:
                stackIndex, stackHeight = stack.pop()
                maxArea = max(maxArea, stackHeight * (pos-stackIndex))
                start = stackIndex
            stack.append((start, height))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i)) 

        return maxArea           
        