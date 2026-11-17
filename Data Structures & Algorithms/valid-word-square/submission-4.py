class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        max_word_len = len(max(words, key = len))
        n = len(words)

        for i in range(n):
            if len(words[i]) != max_word_len:
                diff = max_word_len - len(words[i])
                words[i] += diff * '0'
            else:
                continue    


        for i in range(n):
            word_row = words[i]
            column_word = ''
            for word in words:
               column_word += word[i]
            if word_row == column_word:
                return True
        return False            
        