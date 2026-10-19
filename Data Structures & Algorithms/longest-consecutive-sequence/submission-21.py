class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        setNums = set(nums)
        longestSeq = 0

        for num in setNums:
            if num-1 not in setNums:
                currentNum = num
                currentSeq = 1
                while currentNum+1 in setNums:
                    currentNum += 1
                    currentSeq += 1
                longestSeq = max(currentSeq, longestSeq)

        return longestSeq            
            
           

       