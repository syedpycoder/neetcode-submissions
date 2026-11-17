class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 1
        m = len(flowerbed)
        count = 0
        if m == 1 and flowerbed[-1] == 0:
            if n == 1:
                return True
        while i < m-1:
            if flowerbed[i-1] != 1 and flowerbed[i+1] != 1 and flowerbed[i] == 0:
                count += 1
                flowerbed[i] = 1
            if i == m-2:
                if flowerbed[i-1] != 1 and flowerbed[i] != 1 and flowerbed[i+1] == 0:
                    count += 1
                    flowerbed[i+1] = 1
            i += 1        

        if count == n:
            return True
        return False                

            
