class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        
        n = len(sentence1)
        m = len(sentence2)
       
        if n != m:
            return False
        else:
            for i in range(n):
                if sentence1[i] == sentence2[i]:
                    continue
                elif sentence1[i] != sentence2[i]:
                    if similarPairs:
                        flag = True
                        for j in range(len(similarPairs)):
                            if sentence1[i] in similarPairs[j] and sentence2[i] in similarPairs[j]:
                               flag = False
                               break
                        if flag:
                            return False                       
                    else:
                        return False
            return True                          