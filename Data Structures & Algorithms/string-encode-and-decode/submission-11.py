class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = ''
        for element in strs:
            encode_str += str(len(element))+'#'+element
        return encode_str    

        
    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        n = len(s)

        while i < n:
            j = i
            while s[j] != '#':
                j += 1
            len_str = int(s[i:j])  
            i = j + 1
            j = i + len_str  
            result.append(s[i:j])
            i = j
        return result     

        