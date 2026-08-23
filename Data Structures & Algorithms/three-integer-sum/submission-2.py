class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        sorted_list = sorted(nums)
        n = len(sorted_list)
        triplets = set()

        for i in range(n-1):
            first_num = sorted_list[i]
            j = i + 1
            k = n - 1
            while j < k:
                second_num = sorted_list[j]
                third_num = sorted_list[k]
                target = first_num + second_num + third_num

                if target > 0:
                    k -= 1
                elif target < 0:
                    j += 1
                else:
                    triplets.add((first_num, second_num, third_num))
                    j += 1
                    k -= 1
        return list(triplets)                    

        