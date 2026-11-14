class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        charDict_s = collections.Counter(s)
        charDict_t = collections.Counter(t)

        for ch in charDict_t.keys():
            if ch not in charDict_s:
                return False
            else:
                if charDict_s[ch] != charDict_t[ch]:
                    return False

        return True            

        