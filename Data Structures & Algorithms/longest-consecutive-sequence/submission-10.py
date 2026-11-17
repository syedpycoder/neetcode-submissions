class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        set_num = set(nums)
        max_streak = 0

        for num in set_num:
            current_num = num  
            current_streak = 1  
            while current_num + 1 in set_num:
                current_num += 1
                current_streak += 1    
            max_streak = max(current_streak, max_streak)
        return max_streak        
