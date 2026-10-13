class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        result = []
        for _ in range(2):
            result.extend(nums)
        return result    

        

         