class Solution:
    def confusingNumber(self, n: int) -> bool:
        invalid = ['2','3','4','5','7']
        num_str = str(n)
        for ch in num_str:
            if ch in invalid:
                return False
        return True        
        