class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        elements = path.split('/')
        print(elements)
        result = ""

        for element in elements:
            if element == ".":
                continue
            elif element == "": # /을 기준으로 split 했기에 한 개 이상의 /는 공백으로 처리가 된다
                continue
            elif element == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(element)
        
        result = "/" + "/".join(stack)
        return result