class Solution:

    def encode(self, strs: List[str]) -> str:
        encodeString = ''
        for element in strs:
            encodeString += str(len(element))+'#'+element
        return encodeString    

    def decode(self, s: str) -> List[str]:

        n = len(s)
        i = 0
        result = []

        while i < n:
            j = i
            while s[j] != '#':
                j += 1
            stringLength = int(s[i:j])
            i = j + 1
            j = i + stringLength
            result.append(s[i:j])
            i = j

        return result        
