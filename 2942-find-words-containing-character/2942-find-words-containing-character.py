class Solution(object):
    def findWordsContaining(self, words, x):
        list_x = []
        for index, word in enumerate(words):
            if x in word:
                list_x.append(index)
        return list_x