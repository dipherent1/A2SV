# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        itr = head
        n = 0
        while itr:
            n+=1
            itr = itr.next
        
        ptr = head
        prev = None
        anch = head
        ans = []

        if k>n:
            while ptr:
                prev = ptr
                
                ptr = ptr.next
                
                prev.next = None
                ans.append(prev)
            
            for i in range(k-n):
                ans.append(None)
            return ans
        
        else:
            size = n//k
            extras = n%k
            
            for _ in range(k):
                anch = ptr
                cur_size = size + 1 if extras > 0 else size
                extras-=1
                print(size)
                
                for _ in range((cur_size)):
                    if ptr:
                        prev = ptr
                        ptr= ptr.next
                
                # print(ptr)
                prev.next = None
                ans.append(anch)


        return ans
                    

            
