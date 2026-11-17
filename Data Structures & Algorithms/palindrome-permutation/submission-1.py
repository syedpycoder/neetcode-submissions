class Solution:
    def canPermutePalindrome(self, s: str) -> bool:

        # one element is odd
        # all other element is even
        # all element is even

        charDict = collections.Counter(s)
        countOdd = 0
        countEven = 0

        for ch in charDict:
            if charDict[ch] % 2 == 0:
                countEven += 1
            else:
                countOdd += 1


        if countOdd <=1 or countEven > 0:
            return True

        elif countOdd > 1:
            return False    







    
        