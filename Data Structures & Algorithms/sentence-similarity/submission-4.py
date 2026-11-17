class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:


        if len(sentence1) != len(sentence2):
            return False
        else:
            if similarPairs:
                matchDict = {}
                for element in similarPairs:
                    if element[0] in sentence1:
                       matchDict[element[0]] = element[1]
                    elif element[1] in sentence1:
                        matchDict[element[1]] = element[0]


                for i in range(len(sentence1)):
                    currentVal = sentence1[i]
                    sentence1[i] = matchDict.get(currentVal, '0')

                return ' '.join(sentence1) == ' '.join(sentence2)
            else:
                return True               
        