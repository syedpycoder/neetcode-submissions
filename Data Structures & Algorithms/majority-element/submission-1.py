class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        num_dict = collections.Counter(nums)
        for num in num_dict:
            if num_dict[num] >= n/2:
                return num
            else:
                continue    

       