class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = []
        for num in nums1:
            idx_num = nums2.index(num)
            mapping.append(idx_num)
        return mapping    