class Solution:
    def widestPairOfIndices(self, nums1: List[int], nums2: List[int]) -> int:

        firstSeen = {0:-1}
        difference = 0
        answer = 0

        for i, (a,b) in enumerate(zip(nums1, nums2)):
            difference += a-b

            if difference in firstSeen:
                answer = max(answer, i-firstSeen[difference])
            else:
                firstSeen[difference] = i
        return answer             
