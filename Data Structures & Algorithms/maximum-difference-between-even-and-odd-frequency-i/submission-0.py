class Solution:
    def maxDifference(self, s: str) -> int:

        charDict = collections.Counter(s)
        HighestOdd = 0
        LowestEven = 0

        sorted_freq_des = sorted(charDict.values(), reverse=True)
        sorted_freq_asc = sorted(charDict.values())

        for num in sorted_freq_des:
            if num % 2 == 1:
                HighestOdd = num
                break

        for num in sorted_freq_asc:
            if num % 2 == 0:
                LowestEven = num
                break

        result = HighestOdd - LowestEven
        return result                 





        