class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:

        rows = len(board)
        cols = len(board[0])

        def find():
            crushed_set = set()

            # Search Horizontally

            for r in range(1, rows-1):
                for c in range(cols):
                    if board[r][c] == 0:
                        continue
                    if board[r-1][c] == board[r][c] == board[r+1][c]:
                        crushed_set.add((r-1,c))
                        crushed_set.add((r,c))
                        crushed_set.add((r+1,c))

            # Search Verically

            for r in range(rows):
                for c in range(1, cols-1):
                    if board[r][c] == 0:
                        continue
                    if board[r][c-1] == board[r][c] == board[r][c+1]:
                        crushed_set.add((r,c))
                        crushed_set.add((r,c-1))
                        crushed_set.add((r,c+1))

            return crushed_set            

        def crush(crushed_set):
            for (r,c) in crushed_set:
                board[r][c] = 0

        def drop():
            for c in range(cols):
                lowest_index = -1
                for r in range(rows-1,-1,-1):
                    if board[r][c] == 0:
                        lowest_index = max(lowest_index, r)
                    elif lowest_index >= 0:
                        board[r][c], board[lowest_index][c] = board[lowest_index][c], board[r][c]
                        lowest_index -= 1 

        crushed_set = find()

        while crushed_set:
            crush(crushed_set)
            drop()
            crushed_set = find()

        return board    





        