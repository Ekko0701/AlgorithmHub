# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                return None
            elif not root.left: # 왼쪽 노드가 없으면 오른쪽 노드를 이어 붙인다
                return root.right
            elif not root.right: # 반대로
                return root.left
            
            # 왼쪽 오른쪽 자식이 모두 있는 경우
            else:
                # 오른쪽 서브트리에서 최소값 노드 탐색
                min_larger_node = self.findMin(root.right)
                # 현재 노드의 값을 대체
                root.val = min_larger_node.val
                # 오른쪽 서브트리에서 중복된 노드 삭제
                root.right = self.deleteNode(root.right, min_larger_node.val)

        return root

    def findMin(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node
        