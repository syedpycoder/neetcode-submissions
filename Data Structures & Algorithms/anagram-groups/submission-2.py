class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for element in strs:
            sorted_str = ''.join(sorted(element))
            if sorted_str not in anagram_dict:
                anagram_dict[sorted_str] = [element]
            else:
                anagram_dict[sorted_str].append(element)

        result = list(anagram_dict.values())

        return result            
       