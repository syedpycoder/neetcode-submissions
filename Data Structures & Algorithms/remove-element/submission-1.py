class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pos = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != val:
                nums[pos] = nums[i]
                pos += 1
            else:
                continue
        
        adjust = nums[-1]
        diff = n - pos
        
        for j in range(1, diff):
            nums[-j] = adjust
        
        return pos                
      