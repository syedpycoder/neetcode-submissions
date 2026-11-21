class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        singleList = []
        n = len(grid)
        actualArr = list(range(1, n*n+1))

        for row in grid:
            singleList.extend(row)


        numFreq = collections.Counter(singleList)


        for num in actualArr:
            if numFreq.get(num, 0) == 0:
                b = num
            elif numFreq.get(num, 0) == 2:
                a = num

        return [a, b]

             
            
                     


                    


        