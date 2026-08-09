class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = []
        num_dict = {}
        for pos, num in enumerate(nums2):
            if num not in num_dict:
                num_dict[num] = pos

        for num in nums1:
            mapping.append(num_dict[num])

        return mapping       
