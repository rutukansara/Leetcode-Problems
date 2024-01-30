class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_count = {}
        longest = 0

        for char in s:
            s_count[char] = s_count.get(char, 0) + 1
        

        for c in s_count.values():
            longest += c if c % 2 == 0 else c - 1

        hasOddCount = any(c % 2 == 1 for c in s_count.values())

        return longest+hasOddCount
