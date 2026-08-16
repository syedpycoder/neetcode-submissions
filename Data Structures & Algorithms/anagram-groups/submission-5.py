class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_dict = {}

        for element in strs:
            sorted_element = ''.join(sorted(element))
            if sorted_element not in anagram_dict:
                anagram_dict[sorted_element] = [element]
            else:
                anagram_dict[sorted_element].append(element)

        result = list(anagram_dict.values())

        return result            

        