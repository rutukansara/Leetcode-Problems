class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        for letters in s:
            if letters in vowels:
                s = s.replace(letters, '')
        return s