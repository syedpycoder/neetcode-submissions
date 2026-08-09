class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}
        for num in nums:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                num_dict[num] += 1

        sorted_element = sorted(num_dict.keys(), key = lambda x:num_dict[x], reverse=True)

        top_k_frequent = sorted_element[:k]

        return top_k_frequent            
        