class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        maxArea = 0
        stack = []
        n = len(heights)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                stack_i, stack_h = stack.pop()
                maxArea = max(maxArea, (i-stack_i) * stack_h)
                start = stack_i
            stack.append((start, h))


        for i, h in stack:
            maxArea = max(maxArea, (n-i) * h)

        return maxArea    


       