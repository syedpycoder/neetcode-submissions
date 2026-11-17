class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        maxLeft = []
        maxRight = []
        min_left_right = []
        water = 0

        for i in range(n):
            left = height[:i+1]
            maxLeft.append(max(left))
            if i == n-1:
                maxRight.append(0)
            else:
                right = height[i+1:]
                maxRight.append(max(right)) 
            min_left_right.append(min(maxLeft[i], maxRight[i])) 
            diff = min_left_right[i] - height[i] 
            if diff <= 0:
                continue
            else:
                water += diff            
            
        return water               




       