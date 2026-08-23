class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num_dict = collections.Counter(nums)
        pos = 0

        for num in num_dict:
            if num_dict[num] != 1:
                for _ in range(2):
                    nums[pos] = num
                    pos += 1
            else:
                nums[pos] = num
                pos += 1

        return pos                

        
        