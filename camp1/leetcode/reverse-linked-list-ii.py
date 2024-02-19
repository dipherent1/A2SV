# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        dummy =ListNode()
        dummy.next = head
        l = dummy

        for _ in range(left-1):
            l = l.next

        curr = l.next
        for _ in range(right-left):
            tmp = curr.next
            curr.next = tmp.next
            tmp.next = l.next
            l.next = tmp
        return dummy.next
        