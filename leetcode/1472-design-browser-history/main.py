"""
    1st: stacks
    - maintain 2 stacks, one for backwards and one for forwards
    - when we do back() or forward()
        1. slice the popped array
        2. reverse it
        3. append it to the counter-stack
    
    Time    O(N^2)
    Space   O(N)
    436 ms, faster than 27.01%
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
        steps = min(n-1, steps)
        pops = self.backwards[n-steps:]
        self.backwards = self.backwards[:n-steps]
        self.forwards += pops[::-1]
        return self.backwards[-1]

    def forward(self, steps: int) -> str:
        n = len(self.forwards)
        steps = min(n, steps)
        pops = self.forwards[n-steps:]
        self.forwards = self.forwards[:n-steps]
        self.backwards += pops[::-1]
        return self.backwards[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
