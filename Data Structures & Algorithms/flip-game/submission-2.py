class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        result_str = []
        pos_list = []

        for pos, ch in enumerate(currentState):
            if ch == '+':
                pos_list.append(pos)

        if pos_list:
            n = len(pos_list)
            for i in range(1,n):
                if pos_list[i] - pos_list[i-1] == 1:
                    str_list = list(currentState)
                    str_list[pos_list[i]] = str_list[pos_list[i-1]] = '-'
                    resultantString = ''.join(str_list)
                    result_str.append(resultantString)

        return result_str                    
