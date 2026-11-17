class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 1
        m = len(flowerbed)
        count = 0
        while i < m-1:
            if flowerbed[i-1] != 1 and flowerbed[i+1] != 1:
                count += 1
            if count == n:
                return True      
            i += 1
        return False      

        