class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        flowerbed = [0] + flowerbed + [0]
        m = len(flowerbed)
        countFlower = 0

        for i in range(1, m-1):
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                countFlower += 1
                flowerbed[i] = 1

        return countFlower >= n        

        