class Solution:

    def encode(self, strs: List[str]) -> str:
        result_encode = ''
        for s in strs:
            result_encode += str(len(s))+'#'+s
        return result_encode    
       
       
        
    def decode(self, s: str) -> List[str]:
        result = []
        n = len(s)
        i = 0

        while i < n:
            j = i
            while s[j] != '#':
                j += 1
            string_length = int(s[i:j])
            i = j + 1
            j = i + string_length
            result.append(s[i:j])
            i = j
        return result         
        