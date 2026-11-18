class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        sorted_words = sorted(words, key = len)
        result = set()
        n = len(words)

        for i in range(n):
            for j in range(i+1, n):
                if sorted_words[i] in sorted_words[j]:
                    result.add(sorted_words[i])

        return list(result)         
        