class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)
        result = [0] * n
        stack = []

        for pos, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stackIndex, stackTemp = stack.pop()
                result[stackIndex] = pos - stackIndex
            stack.append((pos, temp))
        return result        

       