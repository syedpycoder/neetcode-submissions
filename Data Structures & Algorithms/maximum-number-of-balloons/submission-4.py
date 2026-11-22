class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        numFreqText = collections.Counter(text)
        numFreqRef = collections.Counter('balloon')

        variations = []

        for ch in numFreqRef:
            if ch in numFreqText:
                combinations = numFreqText[ch] // numFreqRef[ch]
                variations.append(combinations)
            else:
                return 0    

        if not variations:
            return 0
        else:
            return min(variations)        
        