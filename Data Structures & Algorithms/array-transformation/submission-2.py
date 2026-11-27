class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:

        prev = arr[:]

        while True:

            nextArr = prev[:]

            for i in range(1,len(prev) - 1):
                if prev[i] < prev[i-1] and prev[i] < prev[i+1]:
                    nextArr[i] += 1
                elif prev[i] > prev[i-1] and prev[i] > prev[i+1]:
                    nextArr[i] -= 1

            if prev == nextArr:
                break

            prev = nextArr

        return prev                    


        