class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        

        row1 = len(mat1)
        col1 = len(mat1[0])

        row2 = len(mat2)
        col2 = len(mat2[0])

        mat3 = [[0] * col2 for _ in range(row1)]

        tx_mat2 = [[0] * row2 for _ in range(col2)]

        for r in range(row2):
            for c in range(col2):
                tx_mat2[c][r] = mat2[r][c]

        i = 0
        result = 0

        for row in mat1:
            j = 0
            for col in tx_mat2:
                for k in range(len(row)):
                    prod = row[k] * col[k]
                    result += prod
                mat3[i][j] = result
                j += 1
                result = 0
            i += 1

        return mat3            

