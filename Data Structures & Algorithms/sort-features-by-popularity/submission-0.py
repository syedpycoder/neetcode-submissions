class Solution:
    def sortFeatures(self, features: List[str], responses: List[str]) -> List[str]:
        
        charDict = {}

        for response in responses:
            unique_word = set(response.split())
            for word in unique_word:
                if word in features:
                    charDict[word] = charDict.get(word, 0) + 1
                
        sorted_feature = sorted(features, key = lambda x:(-charDict.get(x,0), features.index(x)))

        return sorted_feature            
