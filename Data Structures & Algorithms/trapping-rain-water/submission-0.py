class Solution:
    def trap(self, height: List[int]) -> int:

        water = 0
        n = len(height)

        for i in range(n):
            if height[i] == 0:
                continue
            else:
                left_width = height[i]
                j = i + 1
                
                for k in range(j, n):
                    if height[k] >= left_width:
                        break
                    else:
                        continue    
                right_width = height[k]

                min_fill = min(left_width, right_width)
                print(min_fill)

                for l in range(j,k):
                    water += min_fill - height[l]

        return water                    
        