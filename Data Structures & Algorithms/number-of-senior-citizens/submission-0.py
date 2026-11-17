class Solution:
    def countSeniors(self, details: List[str]) -> int:
        countCitizen = 0

        for detail in details:
            if int(detail[-4:-2]) >= 60:
                countCitizen += 1
        return countCitizen        
        