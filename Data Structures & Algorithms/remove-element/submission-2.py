class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count_val = nums.count(val)
        for _ in range(count_val):
            nums.remove(val)
        return len(nums)    
        