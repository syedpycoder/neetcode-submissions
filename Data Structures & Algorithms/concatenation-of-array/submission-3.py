class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        
        result = []

        for i in range(2):
            result.extend(nums) 

        return result    
      

        