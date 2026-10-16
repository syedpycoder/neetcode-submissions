class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        n = len(board)
        setRow = [set() for _ in range(9)]
        setCol = [set() for _ in range(9)]
        setBox = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                nums = board[i][j]
                if nums == '.':
                    continue
                else:
                    boxId = (i//3)*3 + (j//3)
                    if nums in setRow[i] or nums in setCol[j] or nums in setBox[boxId]:
                        return False
                    setRow[i].add(nums)
                    setCol[j].add(nums)
                    setBox[boxId].add(nums)
        return True                   
        