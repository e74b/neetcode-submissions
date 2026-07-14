import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphaNum = string.ascii_lowercase + string.digits
        right = 0
        left = len(s) - 1
        s = s.lower()

        while right < left:
            while (not s[right].isalnum()) and (right < len(s) - 1):
                right += 1

            while (not s[left].isalnum()) and (left >= 0):
                left -= 1

            if s[right] != s[left]:
                return False
            right += 1
            left -= 1

        return True