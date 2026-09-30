class ListNode:
    def __init__(self, data, back=None, next=None):
        self.data = data
        self.back = back
        self.next = next

class BrowserHistory:
    currentPage = None
    def __init__(self, homepage: str):
        self.currentPage = ListNode(homepage)

    def visit(self, url: str) -> None:
        newNode = ListNode(url)
        self.currentPage.next = newNode
        newNode.back = self.currentPage
        self.currentPage = self.currentPage.next

    def back(self, steps: int) -> str:
        while steps and self.currentPage.back:
            self.currentPage = self.currentPage.back
            steps -= 1
        return self.currentPage.data

    def forward(self, steps: int) -> str:
        while steps and self.currentPage.next:
            self.currentPage = self.currentPage.next
            steps -= 1
        return self.currentPage.data 
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)