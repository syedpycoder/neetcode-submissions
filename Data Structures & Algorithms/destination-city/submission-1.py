class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cityDict = {}
        singleList = []
        for path in paths:
            cityDict[path[0]] = path[1]
            singleList.extend(path)
        setList = set(singleList)
        leftCityList = list(cityDict.keys())   
        for city in setList:
            if city not in leftCityList:
                return city  
    


        
