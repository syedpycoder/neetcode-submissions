class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1Dict = collections.Counter(nums1)
        nums2Dict = collections.Counter(nums2)

        result = []

        for num in nums1Dict:
            if num in nums2Dict:
                result.append(num)

        return result        
        