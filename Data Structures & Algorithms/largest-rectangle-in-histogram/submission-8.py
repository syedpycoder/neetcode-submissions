class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        maxArea = 0
        stack = []
        n = len(heights)

        for pos, height in enumerate(heights):
            start = pos
            while stack and stack[-1][1] > height:
                stackIndex, stackHeight = stack.pop()
                maxArea = max(maxArea, (pos - stackIndex) * stackHeight)
                start = stackIndex
            stack.append((start, height))

        for pos, height in stack:
            maxArea = max(maxArea, (n - pos) * height)

        return maxArea            

       