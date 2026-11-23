class Solution:
    def largestGoodInteger(self, num: str) -> str:

        n = len(num)
        maxValue = "-1"
  

        for i in range(n-2):
            numStr = num[i:i+3]
            if len(set(numStr)) == 1:
                if int(numStr) > int(maxValue):
                    maxValue = numStr
             
                
        if maxValue == "-1":
            return ""
        else:
            return maxValue          
        