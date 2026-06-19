class BrowserHistory:
    # [f,y,g]
    #    ^ 
    # 1
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.actual = 0

    def visit(self, url: str) -> None:
        while self.history[self.actual] != self.history[-1]:
            self.history.pop()

        self.history.append(url)
        self.actual += 1
        return 

    def back(self, steps: int) -> str:
        if steps > self.actual:
            self.actual = 0
            return self.history[0]
        
        self.actual -= steps
        return self.history[self.actual]

    def forward(self, steps: int) -> str:
        if self.actual + steps >= len(self.history):
            self.actual = len(self.history) - 1
            return self.history[-1]

        self.actual += steps
        return self.history[self.actual]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)