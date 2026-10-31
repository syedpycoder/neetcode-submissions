class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:

        min_element = min(nums)
        max_element = max(nums)
        consecutive_list = list(range(min_element, max_element+1))
        return consecutive_list == sorted(nums)
