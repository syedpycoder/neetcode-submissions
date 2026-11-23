class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        result = [[1]]
        for i in range(1, rowIndex+1):
            if i == 1:
                result.append([1,1])    
            else:
                row = result[i-1]
                n = len(row)
                rowBuild = []
                for j in range(1,n):
                    ans = row[j-1] + row[j]
                    rowBuild.append(ans)
                final = [1] + rowBuild + [1]
                result.append(final)
        return result[rowIndex]                
        