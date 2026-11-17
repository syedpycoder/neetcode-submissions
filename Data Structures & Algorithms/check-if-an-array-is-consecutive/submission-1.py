class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:

        min_element = min(nums)
        max_element = max(nums)
        countNums = collections.Counter(nums)
        consecutive_list = list(range(min_element, max_element+1))
        for num in consecutive_list:
            if num not in nums:
                return False
            if countNums[num] != 1:
                return False    
        return True        
