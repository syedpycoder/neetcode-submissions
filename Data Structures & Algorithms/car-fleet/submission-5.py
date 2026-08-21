class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pos_speed = [(pos, speed) for pos, speed in zip(position, speed)]
        stack = []
        sorted_list = sorted(pos_speed, reverse=True)

        for pos, speed in sorted_list:
            time = (target - pos) / speed
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)        
