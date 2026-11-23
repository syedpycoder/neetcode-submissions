class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        freqMagazine = collections.Counter(magazine)
        freqRansom = collections.Counter(ransomNote)

        for ch in freqRansom:
            if freqRansom[ch] > freqMagazine[ch]:
                return False
        return True        
        