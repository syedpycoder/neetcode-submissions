class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        n = len(s)
        charDict = {}

        for i in range(n):
            if s[i] not in charDict:
                # No two charcater may map to same character
                if t[i] in charDict.values():
                    return False
                else:
                    charDict[s[i]] = t[i]
            else:
                if t[i] != charDict[s[i]]:
                    return False
                else:
                    continue
        return True                                