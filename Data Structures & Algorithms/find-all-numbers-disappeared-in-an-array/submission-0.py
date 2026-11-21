class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        n = len(nums)
        actualArr = list(range(1, n+1))
        result = []
        uniqueNum = list(set(nums))
        for num in actualArr:
            if num not in uniqueNum:
                result.append(num)
        return result        
        