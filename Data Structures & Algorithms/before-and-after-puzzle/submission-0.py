class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        result = []
        n = len(phrases)
        for left in range(n):
            first_phrase = phrases[left]
            split_phrase_first = first_phrase.split()
            for right in range(left+1, n):
                second_phrase = phrases[right]
                if second_phrase == first_phrase:
                    result.append(second_phrase)
                else:
                    split_phrase_second = second_phrase.split()
                    if split_phrase_first[-1] == split_phrase_second[0]:
                       final_phrase = first_phrase + " " + ' '.join(split_phrase_second[1:])
                       result.append(final_phrase)
        return result               


