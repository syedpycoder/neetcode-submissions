class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        setRow = [set() for _ in range(9)]
        setCol = [set() for _ in range(9)]
        setBox = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                nums = board[i][j]
                if nums == '.':
                    continue
                else:
                    idBox = (i//3)*3 + (j//3) 
                    if nums in setRow[i] or nums in setCol[j] or nums in setBox[idBox]:
                        return False
                    setRow[i].add(nums)
                    setCol[j].add(nums)
                    setBox[idBox].add(nums)
        return True                   
        