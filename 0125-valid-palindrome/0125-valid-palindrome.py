class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_string = [new_s for new_s in s if new_s.isalnum()]
        clean_string = (''.join(clean_string)).lower()
        left, right = 0, len(clean_string)-1

        while left < right:
            if clean_string[left] != clean_string[right]:
                return False
            else:
                left += 1
                right -= 1
        return True