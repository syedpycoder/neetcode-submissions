class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        count = 0
        setAllowed = set(allowed)
        for word in words:
            setWord = set(word)
            intersectionCheck = setAllowed.intersection(setWord)
            if len(setWord) <= len(intersectionCheck):
                count += 1
        return count        

       