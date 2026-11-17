class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numDict = {}

        for pos, num in enumerate(nums):
            if num not in numDict:
                numDict[num] = pos

        for pos, num in enumerate(nums):
            compliment = target - num
            if compliment in numDict and numDict[compliment] != pos:
                return sorted([numDict[compliment], pos]) 
                
                       


        