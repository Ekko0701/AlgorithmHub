class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = { 
            ')': '(',
            '}': '{',
            ']': '['
        }

        for element in s:
            if element not in table:
                stack.append(element)
            elif not stack or table[element] != stack.pop():
                return False
        return len(stack) == 0