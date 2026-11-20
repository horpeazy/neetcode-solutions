class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeOpenMap = { "]": "[", "}": "{", ")": "("}

        for c in s:
            if c in closeOpenMap:
                if stack and stack[-1] == closeOpenMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False

            
            

        