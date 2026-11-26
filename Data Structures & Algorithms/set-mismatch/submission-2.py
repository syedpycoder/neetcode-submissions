class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        charDict = collections.Counter(nums)
        n = len(nums)
        for num in range(1, n+1):
            if charDict.get(num,0) > 1:
                a = num
            elif charDict.get(num,0) == 0:
                b = num 
        return [a,b]            
        