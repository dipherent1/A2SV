# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head: return 
        read = head
        
        dummy = ListNode(-7000)
        
        while read:
            write = dummy
            
            while write.next and write.next.val < read.val:
                write = write.next
            temp = write.next

            write.next = ListNode(read.val)
            write.next.next = temp

            read = read.next
            # print(head)
        return dummy.next