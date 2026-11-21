class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        unique = set(range(1, len(nums)+1))
        for num in nums:
            unique.discard(num)
        return list(unique)    
        