class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = len(board)
        columns = len(board[0])

        set_row = [set() for _ in range(9)]
        set_col = [set() for _ in range(9)]
        set_box = [set() for _ in range(9)]

        for r in range(rows):
            for c in range(columns):
                num = board[r][c]
                if num == '.':
                    continue
                else:
                    box_id = (r//3)*3+c//3 
                    if num in set_row[r] or num in set_col[c] or num in set_box[box_id]:
                        return False

                    set_row[r].add(num)
                    set_col[c].add(num)
                    set_box[box_id].add(num)
        return True                  

        