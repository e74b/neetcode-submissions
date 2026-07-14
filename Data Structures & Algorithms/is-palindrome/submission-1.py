import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        allowed = string.ascii_lowercase + string.digits
        for letter in s.lower():
            if letter not in allowed:
                continue
            else:
                new_str += letter
    
        for front, back in zip(new_str, new_str[::-1]):
            if front != back:
                return False

        return True