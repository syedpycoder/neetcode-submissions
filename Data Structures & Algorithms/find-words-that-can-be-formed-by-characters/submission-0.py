class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        reference = collections.Counter(chars)
        total = 0
        for word in words:
            wordFreq = collections.Counter(word)
            flag = True
            for ch in wordFreq:
                if ch not in reference:
                    flag = False
                    break
                else:
                    if wordFreq[ch] > reference[ch]:
                       flag = False
            if flag:
                total += len(word)
        return total                
                 
                    
        