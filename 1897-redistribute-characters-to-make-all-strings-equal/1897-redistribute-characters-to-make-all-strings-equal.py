class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count = {}
        for i in range(len(words)):
            for j in words[i]:
                count[j] = count.get(j, 0) + 1
        
        values = list(count.values())

        for value in values:
            if value % len(words):
                return False
        return True

        return values_are_same