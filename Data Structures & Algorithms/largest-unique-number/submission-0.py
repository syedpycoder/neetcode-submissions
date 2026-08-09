class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        num_dict = {}
        sorted_num = sorted(nums, reverse = True)
        for num in nums:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                num_dict[num] += 1

        for num in sorted_num:
            if num_dict[num] == 1:
                return num
        return -1                   
        