class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        n = len(self.nums)
        startSum = 0
        endSum = 0
        self.left = {}
        self.right = {}
        for i in range(n):
            startSum += nums[i]
            self.left[i] = startSum
        for j in range(n-1, 0, -1):
            endSum += nums[j]
            self.right[j] = endSum 
        self.total = sum(self.nums)       

        
        

    def sumRange(self, left: int, right: int) -> int:
        val = self.total -(self.left.get(left-1, 0) + self.right.get(right+1,0))
        return val
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)