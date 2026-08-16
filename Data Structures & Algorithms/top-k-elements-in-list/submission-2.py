class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       

       num_dict = collections.Counter(nums)

       num_keys = list(num_dict.keys())

       sorted_element = sorted(num_keys, key = lambda x:num_dict[x], reverse = True)[:k]

       return sorted_element