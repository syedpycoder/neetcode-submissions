class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        rows = len(words)
        columns = len(max(words, key = len))
        n = max(rows, columns)
        mat = [[0] * n for _ in range(n)]
        i = 0
        for word in words:
            j = 0
            for ch in word:
                mat[i][j] = ch
                j += 1
            i += 1

        for i in range(n):
            for j in range(n):
                if mat[i][j] != mat[j][i]:
                    return False
        return True                    


       