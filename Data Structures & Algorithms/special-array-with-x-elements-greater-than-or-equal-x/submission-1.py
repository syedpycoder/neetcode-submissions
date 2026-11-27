class Solution:
    def specialArray(self, nums: List[int]) -> int:

        numDict = {}
        maxNum = max(nums)
        n = len(nums)

        for num in range(maxNum+1):
            count = 0
            for i in range(n):
                if nums[i] >= num:
                    count += 1
            numDict[num] = count

        for key, value in numDict.items():
            if key == value:
                return key

        return -1                    
        