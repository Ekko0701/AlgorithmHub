class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        num = len(isConnected)
        visited = set()
        count = 0

        def dfs(city):
            for neighbor in range(num):
                if isConnected[city][neighbor] == 1 and neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        for i in range(num):
            if i not in visited:
                count += 1
                visited.add(i)
                dfs(i)
        
        return count