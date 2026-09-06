class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        style = {')':'(', '}':'{', ']':'['}

        for c in s:
            # Is closing
            if c in style:
                if not stack or stack.pop() != style[c]:
                    return False
            # Is opening
            else:
                stack.append(c)
    
        return len(stack) == 0