# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_current = l1
        l2_current = l2
        remain = 0
        
        node = ListNode()
        result_current = node

        while l1_current or l2_current or remain :
            l1_value = 0
            l2_value = 0

            if l1_current:
                l1_value = l1_current.val
            if l2_current:
                l2_value = l2_current.val
                
            value = (l1_value + l2_value) + remain
            remain = value // 10
            current_value = value % 10

            # 노드 추가
            result_current.next = ListNode(current_value)
            result_current = result_current.next

            # 다음 노드로 이동
            if l1_current:
                l1_current = l1_current.next
            if l2_current:
                l2_current = l2_current.next

        return node.next
