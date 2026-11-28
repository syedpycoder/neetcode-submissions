class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        numDict = collections.Counter(nums)
        sortedNums = sorted(nums, key = lambda x:(numDict[x], -x))
        return sortedNums
        