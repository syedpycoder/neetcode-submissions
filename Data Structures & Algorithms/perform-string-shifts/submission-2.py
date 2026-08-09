class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:

        list_string = list(s)
        len_string = len(list_string)

        for direction in shift:
            if direction[1] < len_string:
                if direction[0] == 0:
                   removed_front_part = list_string[:direction[1]]
                   list_string = list_string[direction[1]:] + removed_front_part
                   print(list_string)
                elif direction[0] == 1:
                    removed_last_part = list_string[-direction[1]:]
                    list_string = removed_last_part + list_string[:-direction[1]]
                    print(list_string)
            else:
                print(direction[1])
                continue        
    
        return ''.join(list_string)                

        
        
      