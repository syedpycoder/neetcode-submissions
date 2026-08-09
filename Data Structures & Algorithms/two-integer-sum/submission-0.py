class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for pos, value in enumerate(nums):
            num_dict[value] = pos

        for pos, value in enumerate(nums):
            complement = target - value
            if complement in num_dict and num_dict[complement] != pos:
                return sorted([num_dict[complement], pos])
            else:
                continue        

        