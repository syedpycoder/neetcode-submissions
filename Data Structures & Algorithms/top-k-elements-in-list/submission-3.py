class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        numFreq = collections.Counter(nums)
        numKeys = list(numFreq.keys())

        sortedNums = sorted(numKeys, key = lambda x:numFreq[x], reverse=True)[:k]

        return sortedNums
        