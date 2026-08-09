class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        count_zero = nums.count(0)
        count_one = nums.count(1)
        count_two = nums.count(2)

        for i in range(n):
            if count_zero > 0:
                nums[i] = 0
                count_zero -= 1
            elif count_one > 0:
                nums[i] = 1
                count_one -= 1
            elif count_two > 0:
                nums[i] = 2
                count_two -= 1
