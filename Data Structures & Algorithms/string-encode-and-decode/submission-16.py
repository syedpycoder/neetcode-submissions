class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_string = ''

        for element in strs:
            encode_string += str(len(element)) + '#' + element
        return encode_string    

               
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

       