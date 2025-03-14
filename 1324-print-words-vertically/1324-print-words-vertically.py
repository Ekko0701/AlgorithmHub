class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_len = max(len(word) for word in words)

        result = []
        for i in range(max_len): 
            vertical_word_list = []

            for j in range(len(words)):
                if i < len(words[j]):
                    vertical_word_list.append(words[j][i])
                else:
                    vertical_word_list.append(' ')

            
            vertical_word = ''.join(vertical_word_list).rstrip()
            result.append(vertical_word) 

        return result