class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        reversed_list = []
        for words in s_list:
            words = words[::-1]
            reversed_list.append(words)
        result = " ".join(reversed_list)
        return result