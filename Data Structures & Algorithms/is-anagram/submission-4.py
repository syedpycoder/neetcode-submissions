class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        char_s = collections.Counter(s)
        char_t = collections.Counter(t)

        if len(char_s) != len(char_t):
            return False

        for ch in char_s:
            if ch not in char_t:
                return False
            else:
                if char_s[ch] != char_t[ch]:
                    return False
                else:
                    continue
        return True                        