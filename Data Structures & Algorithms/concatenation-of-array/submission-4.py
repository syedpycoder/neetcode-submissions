class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        ans = []
        for _ in range(2):
            ans.extend(nums)
        return ans    

        
        
        