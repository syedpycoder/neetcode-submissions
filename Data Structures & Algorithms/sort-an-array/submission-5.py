class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        numDict = collections.Counter(nums)
        max_value = max(nums)
        min_value = min(nums)
        index = 0

        for num in range(min_value, max_value+1):
            if num in numDict.keys():
                while numDict[num] > 0:
                    nums[index] = num
                    index += 1
                    numDict[num] -= 1

        return nums            

        