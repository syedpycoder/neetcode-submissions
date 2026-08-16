class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = len(board)
        cols = len(board[0])
        set_row = [set() for _ in range(9)]
        col_row = [set() for _ in range(9)]
        box_row = [set() for _ in range(9)]


        for i in range(rows):
            for j in range(cols):
                num = board[i][j]
                if num == '.':
                    continue
                else:
                    box_id = (i//3) * 3 + (j//3)
                    if num in set_row[i] or num in col_row[j] or num in box_row[box_id]:
                        return False
                    else:
                        set_row[i].add(num)
                        col_row[j].add(num)
                        box_row[box_id].add(num)
        return True                    
                   

        