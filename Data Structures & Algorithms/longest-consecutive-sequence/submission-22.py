class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        setNum = set(nums)
        longestStreak = 0

        for num in setNum:
            if num-1 not in setNum:
                currentNum = num
                currentStreak = 1
                while currentNum+1 in setNum:
                    currentNum += 1
                    currentStreak += 1
                longestStreak = max(currentStreak, longestStreak)

        return longestStreak            
        