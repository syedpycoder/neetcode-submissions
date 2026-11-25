class Solution:
    def isPathCrossing(self, path: str) -> bool:
        cord = [0,0]
        seen = set()
        for direction in path:
            seen.add(tuple(cord))
            if direction == 'N':
                cord[1] += 1
            elif direction == 'E':
                cord[0] += 1
            elif direction == 'S':
                cord[1] -= 1
            elif direction == 'W':
                cord[0] -= 1
            
            if tuple(cord) in seen:
                return True
        
        return False                       
        