class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n):
            right_arr = arr[i+1:]
            if not right_arr:
                arr[i] = -1
            else:
                max_element = max(right_arr)
                arr[i] = max_element
        return arr            
        