class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        result = []
        
        for w in range(len(words)-1, -1, -1):
            result.append(words[w])
            if w != 0:
                result.append(" ")
        
        return ''.join(result)