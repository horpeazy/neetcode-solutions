class ListNode():
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur_page = ListNode(homepage)

    def visit(self, url: str) -> None:
        self.cur_page.next = ListNode(url,self.cur_page)
        self.cur_page = self.cur_page.next
        
    def back(self, steps: int) -> str:
        while self.cur_page.prev and steps > 0:
            self.cur_page = self.cur_page.prev
            steps -= 1

        return self.cur_page.val

    def forward(self, steps: int) -> str:
        while self.cur_page.next and steps > 0:
            self.cur_page = self.cur_page.next
            steps -= 1

        return self.cur_page.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)