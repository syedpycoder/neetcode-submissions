class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def countingSort():
            num_dict = collections.Counter(nums)
            minVal, maxVal = min(nums), max(nums)
            index = 0

            for num in range(minVal, maxVal+1):
                while num_dict[num] > 0:
                    nums[index] = num
                    index += 1
                    num_dict[num] -= 1

        countingSort()

        return nums            