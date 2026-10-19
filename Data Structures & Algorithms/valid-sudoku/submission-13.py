class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        setRow = [set() for _ in range(9)]
        setCol = [set() for _ in range(9)]
        setBox = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                else:
                    boxId = (i//3)*3 + (j//3)
                    if num in setRow[i] or num in setCol[j] or num in setBox[boxId]:
                        return False
                    else:
                        setRow[i].add(num)
                        setCol[j].add(num)
                        setBox[boxId].add(num)
        return True                        
        