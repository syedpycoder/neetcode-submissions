class Solution:
    def removeVowels(self, s: str) -> str:
        
        result = ''
        vowel_list = ['a','e','i','o','u']
        for ch in s:
            if ch not in vowel_list:
                result += ch
        return result         
