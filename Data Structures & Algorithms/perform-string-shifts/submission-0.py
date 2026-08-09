class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
        
        for element in shift:
            
            list_str = list(s)
            if element[0] == 0: 
                list_str = list_str[element[1]:] + list_str[:element[1]]
            elif element[0] == 1:
                list_str = list_str[-element[1]:] + list_str[:-element[1]]
            s = ''.join(list_str) 
        
        return s       

        