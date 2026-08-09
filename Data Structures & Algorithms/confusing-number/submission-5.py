class Solution:
    def confusingNumber(self, n: int) -> bool:
        invalid = ['2','3','4','5','7']
        map_dict = {'0':'0','1':'1','6':'9','8':'8','9':'6'}
        num_str = str(n)
        num = ''
        for ch in num_str:
            if ch in invalid:
                return False
            else:
                num += map_dict[ch]    
        if int(num[::-1]) != n:
            return True
        return False     
        