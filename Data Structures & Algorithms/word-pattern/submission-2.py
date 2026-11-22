class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        split_sentence = s.split()
        if len(pattern) != len(split_sentence):
            return False
        else:
            charDict = {}
            for pos, ch in enumerate(pattern):
                if ch not in charDict:
                    if split_sentence[pos] not in charDict.values():
                       charDict[ch] = split_sentence[pos]
                    else:
                        return False   
                else:
                    if charDict[ch] != split_sentence[pos]:
                        return False
            return True                    

        