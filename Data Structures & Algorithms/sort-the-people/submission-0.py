class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        zippedList = []
        result = []
        for name, height in zip(names, heights):
            zippedList.append([name, height])

        sortedList = sorted(zippedList, key = lambda x:x[1], reverse=True)
        for element in sortedList:
            result.append(element[0])
        return result       
        