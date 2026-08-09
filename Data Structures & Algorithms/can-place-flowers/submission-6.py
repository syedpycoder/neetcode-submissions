class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        flowerbed = [0] + flowerbed + [0]
        m = len(flowerbed)
        i = 1
        count = 0

        while i < m-1:
            if flowerbed[i-1] != 1 and flowerbed[i] != 1 and flowerbed[i+1] != 1:
                count += 1
                flowerbed[i] = 1
            i += 1

        if count >= n:
            return True
        return False            
      
                   