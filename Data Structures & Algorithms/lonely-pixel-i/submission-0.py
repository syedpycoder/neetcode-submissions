class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:

        rows = len(picture)
        cols = len(picture[0])

        tx = [[0] * rows for _ in range(cols)]
        count = 0

        for i in range(rows):
            for j in range(cols):
                tx[j][i] = picture[i][j]

        for i in range(rows):
            for j in range(cols):
                if picture[i][j] == 'B':
                    if picture[i].count('B') == 1 and tx[j].count('B') == 1:
                        count += 1
                else:
                    continue

        return count                

        