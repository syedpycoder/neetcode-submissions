class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        numDict = {}
        n = len(nums)
        result = []

        for num in nums:
            if num not in numDict:
                numDict[num] = 1
            else:
                numDict[num] += 1

        for num in numDict:
            if numDict[num] > n/3:
                result.append(num)
            else:
                continue

        return result             

        