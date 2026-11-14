class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        maxVal = -1
        i = len(arr)-1

        while i >= 0:
            currentVal = arr[i]
            arr[i] = maxVal
            maxVal = max(currentVal, maxVal)
            i -= 1
        return arr    
        