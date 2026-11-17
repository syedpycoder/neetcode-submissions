class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        setNums = sorted(set(nums))
        longestSeq = 0

        for num in setNums:
            startNum = num
            startSeq = 1
            while startNum + 1 in setNums:
                startSeq += 1
                startNum += 1
            longestSeq = max(longestSeq, startSeq)

        return longestSeq        

       