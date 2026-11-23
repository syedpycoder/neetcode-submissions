class Solution:
    def largestGoodInteger(self, num: str) -> str:

        n = len(num)
        result = []
        maxValue = "-1"

        if n < 3:
            return ""
        elif n == 3 and len(set(num)) == 1:
            return num    

        for i in range(n-2):
            numStr = num[i:i+3]
            print(numStr)
            if len(set(numStr)) == 1:
                if int(numStr) > int(maxValue):
                    maxValue = numStr
             
                
        if maxValue == "-1":
            return ""
        else:
            return maxValue          
        