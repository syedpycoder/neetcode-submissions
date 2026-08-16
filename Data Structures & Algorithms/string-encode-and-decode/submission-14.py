class Solution:

    def encode(self, strs: List[str]) -> str:

        encode_string = ''
        for element in strs:
            encode_string += str(len(element)) + '#' + element
        return encode_string    
               
    def decode(self, s: str) -> List[str]:

        n = len(s)
        i = 0
        result = []

        while i < n:
            j = i
            while s[j] != '#':
                j += 1
            
            len_string = int(s[i:j])
            
            i = j + 1
            j = i + len_string
            result.append(s[i:j])
            i = j
    
        return result    

        