class Solution:
    def confusingNumber(self, n: int) -> bool:

        invalid = ['2','3','4','5','7']
        rotation = {'0':'0', '1':'1','6':'9','8':'8','9':'6'}

        num_rotation = ''

        num_str = str(n)

        for ch in num_str:

            if ch in invalid:
                return False
            else:
                num_rotation += rotation[ch]

        if int(num_rotation[::-1]) == n:
            return False
        return True                
        