# cant start with closing parantheses
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for paranthesis in s:
            if paranthesis in '[{(':
                stack.append(paranthesis)
            else:
                if not stack or \
                    (paranthesis == ']' and stack[-1] != '[') or \
                    (paranthesis == '}' and stack[-1] != '{') or \
                    (paranthesis == ')' and stack[-1] != '('):
                        return False
                stack.pop()
        
        return not stack