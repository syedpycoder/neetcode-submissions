class Solution:
    def validWordSquare(self, words: List[str]) -> bool:

        rows = len(words)
        cols = len(max(words, key = len))
        i = 0
        n = max(rows, cols)
        words_tx = [[0] * n for _ in range(n)]

        for word in words:
            for j in range(len(word)):
                words_tx[i][j] = word[j]
            i += 1
        

        for r in range(n):
            for c in range(n):
                if words_tx[r][c] != words_tx[c][r]:
                    return False

        return True                   
        