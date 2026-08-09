class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_count = {}
        n = len(nums)
        for num in nums:
            if num not in num_count:
                num_count[num] = 1
            else:
                num_count[num] += 1

        for num,value in num_count.items():
            if value >= n/2:
                return num

        