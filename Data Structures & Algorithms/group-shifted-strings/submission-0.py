class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        group_dict = {}

        def get_hash(string):
            key = []
            for a,b in zip(string, string[1:]):
                key.append(chr((ord(b)-ord(a)) % 26 + 97))
            return ''.join(key)

        for string in strings:
            hash_value = get_hash(string)
            if hash_value not in group_dict:
                group_dict[hash_value] = [string]
            else:
                group_dict[hash_value].append(string)

        return list(group_dict.values())                    
        