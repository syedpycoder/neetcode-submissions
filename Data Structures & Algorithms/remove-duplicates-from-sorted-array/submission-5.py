class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        num_dict = {}
        for num in nums:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                continue

        list_num = list(num_dict.keys())
        k = len(list_num)

        for i in range(k):
            nums[i] = list_num[i]

        return k                  
       