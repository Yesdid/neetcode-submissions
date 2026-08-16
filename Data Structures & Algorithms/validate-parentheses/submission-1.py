class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matchingParen = {")":"(", "]":"[", "}":"{"}

        for c in s:
            if c in matchingParen:
                if len(stack) != 0 and stack[-1] == matchingParen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if len(stack) != 0:
            return False
        return True