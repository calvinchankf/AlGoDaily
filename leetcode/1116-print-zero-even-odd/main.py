from threading import Lock, Semaphore

"""
    1st: use Mutex Lock to deal with concurrency
    keep in mind: zero(), even(), odd() will only be called once on each cooresponding thread
    12 ms, faster than 99.22%
"""


class ZeroEvenOdd(object):
    def __init__(self, n):
        self.n = n
        self.num = 1

        self.zeroLock = Lock()
        self.oddLock = Lock()
        self.evenLock = Lock()

        self.oddLock.acquire()
        self.evenLock.acquire()

    def zero(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for _ in range(self.n):
            self.zeroLock.acquire()
            printNumber(0)
            if self.num % 2 == 0:
                self.evenLock.release()
            else:
                self.oddLock.release()

    def even(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for _ in range(self.n//2):
            self.evenLock.acquire()
            printNumber(self.num)
            self.num += 1
            self.zeroLock.release()

    def odd(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for _ in range((self.n+1)//2):
            self.oddLock.acquire()
            printNumber(self.num)
            self.num += 1
            self.zeroLock.release()


"""
    2nd: use Semaphore to deal with concurrency
    keep in mind: zero(), even(), odd() will only be called once on each cooresponding thread
    40 ms, faster than 36.64%
"""


class ZeroEvenOdd(object):
    def __init__(self, n):
        self.n = n
        self.num = 1
        self.zeroLock = Semaphore(1)
        self.oddLock = Semaphore(0)
        self.evenLock = Semaphore(0)

        # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for _ in range(self.n):
            self.zeroLock.acquire()
            printNumber(0)
            if self.num % 2 == 0:
                self.evenLock.release()
            else:
                self.oddLock.release()

    def even(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for _ in range(self.n//2):
            self.evenLock.acquire()
            printNumber(self.num)
            self.num += 1
            self.zeroLock.release()

    def odd(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for _ in range((self.n+1)//2):
            self.oddLock.acquire()
            printNumber(self.num)
            self.num += 1
            self.zeroLock.release()
