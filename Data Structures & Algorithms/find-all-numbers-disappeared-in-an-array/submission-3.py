class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        n = len(nums)
        actualArr = list(range(1, n+1))
        setNum = set(nums)
        result = []

        for num in actualArr:
            if num not in setNum:
                result.append(num)

        return result        
        