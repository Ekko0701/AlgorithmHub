# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def bfs(target):
            if not target:
                return []
            
            result = []
            queue = deque([target])
            level = 0

            while queue:
                level_size = len(queue)
                level_result = []

                for _ in range(level_size):
                    node = queue.popleft()
                    level_result.append(node.val)

                    if node.left:
                        queue.append(node.left)
                    
                    if node.right:
                        queue.append(node.right)

                result.append(level_result)
                level += 1

            return result

        result = bfs(root)
        answer = []

        for i in range(len(result)):
            answer.append(result[i][-1])
        
        return answer