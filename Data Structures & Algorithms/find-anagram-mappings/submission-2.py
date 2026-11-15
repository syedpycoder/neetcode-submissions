class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:

        pos_dict = {}
        result = [] 
        for pos, num in enumerate(nums2):
            if num not in pos_dict:
                pos_dict[num] = [pos]
            else:
                pos_dict[num].append(num)

        for num in nums1:
            result.append(pos_dict[num][0])

        return result             




        