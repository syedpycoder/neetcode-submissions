class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        result = [[1]]
        for i in range(1, numRows):
            newRow = []
            for j in range(i+1):
                if j == 0 or j == i:
                    newRow.append(1)
                else:
                    lastRow = result[-1]
                    #print(lastRow)
                    #print(j)
                    total = lastRow[j-1] + lastRow[j]
                    newRow.append(total)
            result.append(newRow)
        return result                
        