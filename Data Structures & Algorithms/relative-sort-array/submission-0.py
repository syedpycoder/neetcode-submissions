class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        numDict = collections.Counter(arr1)
        orderArr2 = []
        orderArr1 = []
        for num in arr2:
            orderArr2.extend([num]*numDict[num])
        for num in arr1:
            if num not in arr2:
                orderArr1.append(num)
       
        sortedList = sorted(orderArr1)
        result = orderArr2 + sortedList
        return result     
          
        