class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        set_rows = [set() for _ in range(9)]
        set_cols = [set() for _ in range(9)]
        set_box = [set() for _ in range(9)]


        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                else:
                    box_id = (i//3) * 3 + (j//3)
                    if num in set_rows[i] or num in set_cols[j] or num in set_box[box_id]:
                        return False
                    else:
                        set_rows[i].add(num)
                        set_cols[j].add(num)
                        set_box[box_id].add(num)
        return True                         
       