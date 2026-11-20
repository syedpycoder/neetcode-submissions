class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        numDict = {}
        result = []
        n = len(nums2)
        
        for pos, num in enumerate(nums2):
            numDict[num] = pos

        for num in nums1:
            indexNum = numDict[num]
            nextGreater = -1
            for j in range(indexNum, n):
                if nums2[j] > num:
                    nextGreater = nums2[j]
                    break
            result.append(nextGreater)        
        return result                 

        