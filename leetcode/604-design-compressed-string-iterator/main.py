class StringIterator:

    def __init__(self, compressedString: str):
        self.s = compressedString
        self.c = ''

    def next(self) -> str:
        if len(self.s) == 0 and len(self.c) == 0:
            return " "

        if len(self.c) == 0:
            c = self.s[0]
            self.s = self.s[1:]
            num = 0
            while len(self.s) > 0 and self.s[0].isdigit():
                x = self.s[0]
                self.s = self.s[1:]
                num = num * 10 + int(x)
            self.c = num * c

        res = self.c[0]
        self.c = self.c[1:]
        return res

    def hasNext(self) -> bool:
        if len(self.s) == 0 and len(self.c) == 0:
            return False
        return True


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
