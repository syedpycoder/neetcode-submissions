class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        charDict = collections.Counter(s)
        total = 0
        freqVal = sorted(charDict.values(), reverse=True)
        flag = True

        for num in freqVal:
            if flag and num % 2 != 0:
                total += num
                flag = False
            elif num % 2 != 0:
                total += num-1    
            elif num % 2 == 0:
                total += num


        return total            