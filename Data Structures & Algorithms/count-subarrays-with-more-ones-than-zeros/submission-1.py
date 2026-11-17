class Solution:
    def subarraysWithMoreOnesThanZeroes(self, nums: List[int]) -> int:

        numDict = {0:0, 1:0}
        count = 0

        for num in nums:
            if num == 0:
                numDict[0] += 1
            else:
                numDict[1] += 1


            if numDict[1] > numDict[0]:
                if num == 1:
                    count += numDict[1]
                else:
                    count += numDict[0]    

        return count               
