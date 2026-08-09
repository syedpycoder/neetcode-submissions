class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        shift_dict = {}

        def get_hash(string_name):
            result = []
            for a, b in zip(string_name, string_name[1:]):
                result.append(chr(((ord(b)-ord(a)) % 26) + 97))
            return ''.join(result)    


        for string in strings:
            value = get_hash(string)
            if value not in shift_dict:
                shift_dict[value] = [string]
            else:
                shift_dict[value].append(string)

        result = list(shift_dict.values())

        return result                