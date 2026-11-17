class Solution:
    def arrangeCoins(self, n: int) -> int:

        i = 0
        arr = [0] * n
        val = n
        sum_i = 0
        count = 0

        while n >= 0:
            if n > i:
                arr[i] = i + 1
            else:
                arr[i] = n

            if arr[i] == i + 1:
                count += 1

            i += 1
            sum_i += i
            n -= sum_i
        
        return count    



           

