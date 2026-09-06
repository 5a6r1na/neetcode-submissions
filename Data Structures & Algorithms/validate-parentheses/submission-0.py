class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        style = {'(':')', '{':'}', '[':']'}

        for c in s:
            # check if opening
            if c in style:
                stack.append(c)
            # check prev style for closing
            else:
                if len(stack) == 0:
                    return False
                prev = stack.pop()
                if style.get(prev) != c:
                    return False
    
        return len(stack) == 0