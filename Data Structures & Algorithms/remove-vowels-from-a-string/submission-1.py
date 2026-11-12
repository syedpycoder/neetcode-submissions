class Solution:
    def removeVowels(self, s: str) -> str:
        
        for ch in s:
            if ch in 'aeiou':
                s = s.replace(ch, '')
        return s        
