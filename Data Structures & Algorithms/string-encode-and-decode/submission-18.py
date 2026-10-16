class Solution:

    def encode(self, strs: List[str]) -> str:

        encodeString = ''
        for element in strs:
            encodeString += str(len(element))+'#'+element
        return encodeString    

    def decode(self, s: str) -> List[str]:
        n = len(s)
        result = []
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
