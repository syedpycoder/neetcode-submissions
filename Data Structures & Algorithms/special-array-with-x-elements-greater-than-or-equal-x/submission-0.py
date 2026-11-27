class Solution:
    def specialArray(self, nums: List[int]) -> int:

        maxNum = max(nums)
        numDict = {}
        n = len(nums)
        for num in range(maxNum+1):
            count = 0
            for i in range(n):
                if nums[i] >= num:
                    count += 1
            numDict[num] = count

        for pos, val in numDict.items():
            if pos == val:
                return pos

        return -1                    
        