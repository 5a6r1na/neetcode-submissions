class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean = ''.join(filter(str.isalnum, s)).lower()
        front = 0
        back = len(clean) - 1 


        while front < back:
            if clean[front] != clean[back]:
                return False
            else:
                front += 1
                back -= 1
        

        return True