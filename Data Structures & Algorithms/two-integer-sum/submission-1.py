class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for pos,val in enumerate(nums):
            if val not in num_dict:
                num_dict[val] = pos
            else:
                continue

        for pos, val in enumerate(nums):
            compliment = target - val
            if compliment in num_dict and num_dict[compliment] != pos:
                return sorted([num_dict[compliment], pos])
                             