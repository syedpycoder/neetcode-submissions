class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        shift_dict = {}

        def get_hash(string):
            result = []
            for a, b in zip(string, string[1:]):
                diff = (ord(b) - ord(a)) % 26 + 97
                result.append(chr(diff))
            return ''.join(result)

        for string in strings:
            hash_value = get_hash(string)
            if hash_value not in shift_dict:
                shift_dict[hash_value] = [string]
            else:
                shift_dict[hash_value].append(string)


        result = list(shift_dict.values()) 

        return result               

               