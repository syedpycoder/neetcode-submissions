class Solution:

    def encode(self, strs: List[str]) -> str:
        single_string = ''
        for element in strs:
            single_string += element + '+'
        return single_string    

    def decode(self, s: str) -> List[str]:
        return s[:-1].split('+')
        
     