class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        num_dict = collections.Counter(nums)
        result = []
        min_num = min(nums)
        max_num = max(nums)

        for num in range(min_num, max_num+1):
            result.extend([num] * num_dict.get(num, 0))

        return result    
        