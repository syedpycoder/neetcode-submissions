class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_dict = {}

        for pos, value in enumerate(nums):
            if value not in num_dict:
                num_dict[value] = pos
            else:
                continue


        for pos, value in enumerate(nums):
            complement = target - value
            if complement in num_dict and num_dict[complement] != pos:
                return sorted([pos, num_dict[complement]])

