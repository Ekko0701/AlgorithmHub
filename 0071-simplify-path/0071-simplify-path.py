class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = deque()
        elements = path.split('/')
        result = ""

        for element in elements:
            if element == "..":
                if stack:
                    stack.pop()
            elif element and element != '.':
                stack.append(element)
        
        result = "/" + "/".join(stack)
        return result