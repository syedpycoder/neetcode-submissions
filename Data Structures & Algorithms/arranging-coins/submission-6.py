class Solution:
    def arrangeCoins(self, n: int) -> int:

        i = 0
        arr = []
        val = n
        sum_i = 0
        count = 0

        while n > 0:
            if n > sum_i:
               arr.append(i+1)
            else:
               arr.append(n)

            if arr[-1] == i + 1:
                count += 1

            i += 1
            sum_i += i
            n -= sum_i
        
        return count    



           

