class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        char_s = collections.Counter(list(s))
        char_t = collections.Counter(list(t))
        set_t = set(list(t))

        if len(char_s) != len(char_t):
            return False

        for ch in set_t:
            if ch not in char_s:
                return False
            elif ch in char_s:
                if char_s[ch] != char_t[ch]:
                    return False
                else:
                    continue
        return True                




        