class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s))+'#'+s
        return res    
       
        
    def decode(self, s: str) -> List[str]:
        result = []
        n = len(s)
        i = 0

        while i < n:
            j = i
            while s[j] != '#':
                j += 1
            length_string = int(s[i:j])
            i = j + 1
            j = i + length_string
            result.append(s[i:j])
            i = j
        return result                  