class Solution:
    def isCircularSentence(self, sentence: str) -> bool:

        sentenceSplit = sentence.split()
        n = len(sentenceSplit)
        flag = False

        for i in range(n):
            print(i)
            if i == n-1:
                if sentenceSplit[i][-1] == sentenceSplit[0][0]:
                    flag = True
                else:
                    return False
            else:
                if sentenceSplit[i][-1] == sentenceSplit[i+1][0]:
                    flag = True
                else:
                    return False
        return flag                            
               

