class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        numFreqText = collections.Counter(text)
        numFreqRef = collections.Counter('balloon')

        variations = []

        for ch in numFreqRef:
            if ch in numFreqText:
                print(ch)
                print(numFreqText[ch])
                print(numFreqRef[ch])
                combinations = numFreqText[ch] // numFreqRef[ch]
                print(combinations)
                variations.append(combinations)
                print(variations)
            else:
                return 0    

        if not variations:
            return 0
        else:
            return min(variations)        
        