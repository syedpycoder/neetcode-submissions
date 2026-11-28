class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        setNums1 = set(nums1)
        setNums2 = set(nums2)
        intersection = setNums1.intersection(setNums2)

        for element in intersection:
            setNums1.discard(element)
            setNums2.discard(element)

        return [list(setNums1), list(setNums2)]    

        