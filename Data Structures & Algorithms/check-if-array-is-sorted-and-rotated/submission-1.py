class Solution:
    def check(self, nums: List[int]) -> bool:

        sortedNums = sorted(nums)
        n = len(nums)
        if nums == sortedNums:
            return True
        else:
            for _ in range(n):
                val = nums.pop(0)
                nums.append(val)
                if nums == sortedNums:
                    return True
            return False            
        