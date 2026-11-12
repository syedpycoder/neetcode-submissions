class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        minNum = str(min(nums))
        result = 0

        for ch in minNum:
            result += int(ch)

        if result % 2 == 0:
            return 1
        return 0    
