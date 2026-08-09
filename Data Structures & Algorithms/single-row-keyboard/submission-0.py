class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        distance_map = {}

        for pos, ch in enumerate(keyboard):
            distance_map[ch] = pos
            
        current_pos = 0
        total_distance = 0

        for ch in word:
            total_distance += abs(distance_map[ch] - current_pos)
            current_pos = distance_map[ch]

        return total_distance        
        