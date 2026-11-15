class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:


        if len(sentence1) != len(sentence2):
            return False
        else:
            if similarPairs:
                matchDict = {}
                for element in similarPairs:
                    if element[0] in sentence1 and element[1] in sentence2:
                        if element[0] not in matchDict:
                            matchDict[element[0]] = [element[1]]
                        else:
                            matchDict[element[0]].append(element[1])    
                    if element[1] in sentence1 and element[0] in sentence2:
                        if element[1] not in matchDict:
                            matchDict[element[1]] = [element[0]]
                        else:
                            matchDict[element[1]].append(element[0])    

                for i in range(len(sentence1)):
                    currentVal1 = sentence1[i]
                    currentVal2 = sentence2[i]
                    if currentVal1 == currentVal2:
                        continue
                    else:
                        if currentVal1 in matchDict and currentVal2 in matchDict[currentVal1]:
                            continue
                        else:
                            return False
                return True            
            else:
                return sentence1 == sentence2                
