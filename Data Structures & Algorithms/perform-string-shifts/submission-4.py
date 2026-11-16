class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:

        list_string = list(s)
        for i in range(len(shift)):
            operation = shift[i]
            direction = operation[0]
            amount = operation[1]
            if direction == 0:
                if amount > 0:
                    list_string = list_string[amount:] + list_string[:amount]
            elif direction == 1:
                if amount > 0:
                    list_string = list_string[-amount:] + list_string[:-amount] 
        final_string = ''.join(list_string)
        return final_string                   
        