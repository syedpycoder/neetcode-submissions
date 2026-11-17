class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        max_word_len = len(max(words, key = len))
        n = len(words)

        for i in range(n):
            if len(words[i]) != max_word_len:
                words[i] += (max_word_len - len(words[i])) * '0'
            else:
                continue    


        for i in range(n):
            word_row = words[i]
            column_word = ''
            for j in range(n):
               word = words[j]
               column_word += word[i]
            if word_row == column_word:
                return True
        return False            
        