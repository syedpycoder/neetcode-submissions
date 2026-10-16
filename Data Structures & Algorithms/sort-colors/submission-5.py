class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        numDict = collections.Counter(nums)
        n = len(nums)

        for i in range(n):

            if numDict[0] > 0:
                nums[i] = 0
                numDict[0] -= 1
            elif numDict[1] > 0:
                nums[i] = 1
                numDict[1] -= 1
            else:
                nums[i] = 2
                numDict[2] -= 1
                        
        