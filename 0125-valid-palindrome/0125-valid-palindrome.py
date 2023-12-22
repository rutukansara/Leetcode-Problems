class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().strip()
        new_s = [n_s for n_s in s if n_s.isalnum()]
        new_s = "".join(new_s)
        if new_s == new_s[::-1]:
            return True
        return False