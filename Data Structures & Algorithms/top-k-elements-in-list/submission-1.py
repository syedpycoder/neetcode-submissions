class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       

       num_dict = collections.Counter(nums)

       num_key = list(num_dict.keys())

       sorted_num = sorted(num_key, key = lambda x:num_dict[x], reverse=True)[:k]

       return sorted_num