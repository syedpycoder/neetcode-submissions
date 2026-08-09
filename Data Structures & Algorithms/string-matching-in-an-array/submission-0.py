class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        n = len(words)
        result = []

        for i in range(n):
            ref_word = words[i]
            for j in range(n):
                if j == i:
                    continue
                else:
                    if ref_word in words[j]:
                        result.append(ref_word)
                        break
        return result                    

        