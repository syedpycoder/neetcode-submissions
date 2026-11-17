class Solution:
    def appendCharacters(self, s: str, t: str) -> int:


        char_t_count = len(t)
        char_s_count = 0

        for i in range(char_t_count):
            if t[i] == s[char_s_count]:
                char_s_count += 1
            else:
                continue
        req = char_t_count - char_s_count
        return req            
    

       