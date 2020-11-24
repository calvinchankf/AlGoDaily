"""
    1st: stacks
    - maintain 2 stacks, one for backwards and one for forwards
    - when we do back() or forward()
        1. slice the popped array
        2. reverse it
        3. append it to the counter-stack
    
    Time    O(N^2)
    Space   O(N)
    296 ms, faster than 32.74%
"""


class BrowserHistory:

    def __init__(self, homepage: str):
        self.backwards = [homepage]
        self.forwards = []

    def visit(self, url: str) -> None:
        self.backwards.append(url)
        if len(self.forwards) > 0:
            self.forwards = []

    def back(self, steps: int) -> str:
        n = len(self.backwards)
        k = max(n - steps, 1)
        pops = self.backwards[k:]
        self.backwards = self.backwards[:k]
        while len(pops) > 0:
            self.forwards.append(pops.pop())
        return self.backwards[-1]

    def forward(self, steps: int) -> str:
        n = len(self.forwards)
        k = max(n - steps, 0)
        pops = self.forwards[k:]
        self.forwards = self.forwards[:k]
        while len(pops) > 0:
            self.backwards.append(pops.pop())
        return self.backwards[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
