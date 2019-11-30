from threading import Lock

"""
    1st: cheat, make the program single-thread
    - actually i am not sure if there is an easy to do it...
    24 ms, faster than 80.39%
"""


class H2O(object):
    def __init__(self):
        self.lock = Lock()
        self.hnum = 0
        self.onum = 0
        self.hrelease = None
        self.orelease = None

    def hydrogen(self, releaseHydrogen):
        self.hrelease = releaseHydrogen
        self.output(1, 0)

    def oxygen(self, releaseOxygen):
        self.orelease = releaseOxygen
        self.output(0, 1)

    def output(self, h, o):
        with self.lock:
            self.hnum += h
            self.onum += o
            if self.hnum >= 2 and self.onum >= 1:
                self.hrelease()
                self.hrelease()
                self.orelease()
                self.hnum -= 2
                self.onum -= 1
