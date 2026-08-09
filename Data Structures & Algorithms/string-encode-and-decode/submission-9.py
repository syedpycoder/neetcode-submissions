class Solution:

    def encode(self, strs: List[str]) -> str:

        result_encode = ''

        for element in strs:
            result_encode += str(len(element))+'#'+element

        return result_encode    


        
    def decode(self, s: str) -> List[str]:

        result = []
        i = 0
        n = len(s)

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
       