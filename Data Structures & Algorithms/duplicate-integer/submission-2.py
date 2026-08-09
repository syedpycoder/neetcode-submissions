class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_count = collections.Counter(nums)
        for num in num_count:
            if num_count[num] != 1:
                return True
        return False        
       