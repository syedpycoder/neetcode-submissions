class Solution:
    def countElements(self, arr: List[int]) -> int:
        sort_arr = sorted(set(arr))
        count = 0
        n = len(sort_arr)

        for i in range(n-1):
            if sort_arr[i] + 1 == sort_arr[i+1]:
                count += 1

        return count        
        