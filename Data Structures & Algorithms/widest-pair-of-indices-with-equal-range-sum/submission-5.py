class Solution:
    def widestPairOfIndices(self, nums1: List[int], nums2: List[int]) -> int:

        prefix = {0:-1}
        answer = 0
        diff = 0

        for i, (a,b) in enumerate(zip(nums1, nums2)):

            diff += a - b

            if diff in prefix:
                answer = max(answer, i-prefix[diff])
            else:
                prefix[diff] = i

        return answer            
