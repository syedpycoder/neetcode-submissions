class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        charDict = collections.Counter(arr)

        for element in arr:
            if charDict[element] == 1:
                k -= 1
                if k == 0:
                    return element
        return ""            
        