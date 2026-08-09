class Solution:
    def countElements(self, arr: List[int]) -> int:
        sort_arr = sorted(set(arr))
        count = 0
        n = len(sort_arr)

        char_dict = {}
        for num in arr:
            if num not in char_dict:
                char_dict[num] = 1
            else:
                char_dict[num] += 1    

        for i in range(n-1):
            if sort_arr[i] + 1 == sort_arr[i+1]:
                freq = char_dict[sort_arr[i]]
                count += freq

        return count        
        