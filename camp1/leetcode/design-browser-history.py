class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class BrowserHistory:

    def __init__(self, homepage: str):
        self.home = ListNode(homepage)
        self.cur = self.home

    def visit(self, url: str) -> None:
        v = ListNode(url)
        v.next = None
        v.prev = self.cur
        self.cur.next = v
        self.cur = v
        
    def back(self, steps: int) -> str:
        while self.cur.prev and steps:
            self.cur = self.cur.prev
            steps-=1

        return self.cur.val

    def forward(self, steps: int) -> str:
        while self.cur.next and steps:
            self.cur = self.cur.next
            steps-=1

        return self.cur.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)