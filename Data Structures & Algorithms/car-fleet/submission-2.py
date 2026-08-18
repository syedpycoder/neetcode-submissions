class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pos_speed_list = [(pos,speed) for pos, speed in zip(position, speed)]
        sorted_list = sorted(pos_speed_list, reverse=True)
        stack = []

        for pos, speed in sorted_list:
            time = (target-pos)/speed
            stack.append(time)
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()
        return len(stack)    

         