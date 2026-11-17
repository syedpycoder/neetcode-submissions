class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        n = len(temperatures)
        result = []

        for i in range(n):
            stack.append(temperatures[i])
            j = i+1
            count = 1
            greater_temp = False
            while j < n:
                if temperatures[j] <= stack[-1]:
                    count += 1
                else:
                    greater_temp = True
                    result.append(count)
                    break
                j += 1    
            if not greater_temp:
                result.append(0)
            stack.pop()    
        return result                  
                    
        
        