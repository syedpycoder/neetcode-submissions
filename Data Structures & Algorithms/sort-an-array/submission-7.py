class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        maxNum = max(nums)
        minNum = min(nums)

        num_dict = collections.Counter(nums)

        index = 0

        for num in range(minNum, maxNum+1):
            while num_dict[num] > 0:
                nums[index] = num
                index += 1
                num_dict[num] -= 1

        return nums        
       