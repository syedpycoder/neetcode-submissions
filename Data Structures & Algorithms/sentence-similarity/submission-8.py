class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:


        if len(sentence1) != len(sentence2):
            return False
        else:
            if similarPairs:
                matchDict = {}
                for element in similarPairs:
                    if element[0] in sentence1 and element[1] in sentence2:
                        matchDict[element[0]] = element[1]  
                    elif element[1] in sentence1 and element[0] in sentence2:
                        matchDict[element[1]] = element[0]
                print(matchDict)        
                for i in range(len(sentence1)):
                    currentVal1 = sentence1[i]
                    currentVal2 = sentence2[i]
                    if currentVal1 == currentVal2:
                        continue
                    else:
                        if currentVal1 in matchDict:
                           sentence1[i] = matchDict[currentVal1]
                        else:
                           return False
                return ' '.join(sentence1) == ' '.join(sentence2)            

            else:
                return True               
        