class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        result = set()
        n = len(phrases)
        for left in range(n):
            phrase_split_first = phrases[left].split()
            for right in range(n):
                if left == right:
                    continue
                phrase_split_second = phrases[right].split()
                if phrase_split_first[-1] == phrase_split_second[0]:
                    combined = phrase_split_first + phrase_split_second[1:]
                    result.add(' '.join(combined))
        return sorted(result)            



