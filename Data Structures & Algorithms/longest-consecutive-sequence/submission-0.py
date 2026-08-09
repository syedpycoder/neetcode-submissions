class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longest = 0
        numSet = set(nums)
        for num in numSet:
            if num-1 not in numSet:
                start_seq = num
                current_streak = 1
                while start_seq + current_streak in numSet:
                    current_streak += 1
                longest = max(current_streak, longest)
        return longest            

                
            