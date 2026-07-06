class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for letter in s:
            if letter == "(":
                stack.append(")")
            elif letter == "{":
                stack.append("}")
            elif letter == "[":
                stack.append("]")

            if letter in ["]", "}", ")"]:
                if len(stack) == 0:
                    return False
                if stack.pop(-1) != letter:
                    return False

        if len(stack) > 0:
            return False

        return True