# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        cur = head
        ans = ListNode()
        
        while cur:
            new = ListNode(cur.val)
            new.next = ans.next
            ans.next = new            
            cur = cur.next
        return ans.next
        