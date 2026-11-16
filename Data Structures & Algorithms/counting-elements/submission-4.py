class Solution:
    def countElements(self, arr: List[int]) -> int:

        countNum = 0

        #0th index has arr[0] + 1 ==> 2
        #1th index has arr[1] + 1 ==> 3

        for i in range(len(arr)):
            if arr[i] + 1 in arr:
                countNum += 1

        return countNum        

        