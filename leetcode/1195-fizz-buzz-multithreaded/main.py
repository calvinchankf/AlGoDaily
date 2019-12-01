from threading import Lock
from threading import Semaphore

"""
    1st: use Mutex Lock to deal with concurrency
    keep in mind: foo(), bar() will only be called once on each cooresponding thread
    20 ms, faster than 83.23% 
"""


class FizzBuzz(object):
    def __init__(self, n):
        self.n = n

        self.numLock = Lock()
        self.fizzLock = Lock()
        self.buzzLock = Lock()
        self.fizzbuzzLock = Lock()

        self.fizzLock.acquire()
        self.buzzLock.acquire()
        self.fizzbuzzLock.acquire()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz):
        """
        :type printFizz: method
        :rtype: void
        """
        for i in range(1, self.n+1):
            if i % 3 == 0 and i % 5 > 0:
                self.fizzLock.acquire()
                printFizz()
                self.numLock.release()

    # printBuzz() outputs "buzz"

    def buzz(self, printBuzz):
        """
        :type printBuzz: method
        :rtype: void
        """
        for i in range(1, self.n+1):
            if i % 3 > 0 and i % 5 == 0:
                self.buzzLock.acquire()
                printBuzz()
                self.numLock.release()

    # printFizzBuzz() outputs "fizzbuzz"

    def fizzbuzz(self, printFizzBuzz):
        """
        :type printFizzBuzz: method
        :rtype: void
        """
        for i in range(1, self.n+1):
            if i % 3 == 0 and i % 5 == 0:
                self.fizzbuzzLock.acquire()
                printFizzBuzz()
                self.numLock.release()

    # printNumber(x) outputs "x", where x is an integer.

    def number(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1, self.n+1):
            self.numLock.acquire()
            if i % 3 == 0 and i % 5 == 0:
                self.fizzbuzzLock.release()
            elif i % 3 == 0:
                self.fizzLock.release()
            elif i % 5 == 0:
                self.buzzLock.release()
            else:
                printNumber(i)
                self.numLock.release()


"""
    2nd: use Semaphore to deal with concurrency

    keep in mind:
    - Semaphore(x) where x is capacity
    - semaphore.acquire() means locks -= 1
    - semaphore.release() means locks += 1

    8 ms, faster than 100.00%
"""


class FizzBuzz(object):
    def __init__(self, n):
        self.n = n
        self.numLock = Semaphore(1)
        self.fizzLock = Semaphore(0)
        self.buzzLock = Semaphore(0)
        self.fizzbuzzLock = Semaphore(0)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz):
        """
        :type printFizz: method
        :rtype: void
        """
        for i in range(1, self.n+1):
            if i % 3 == 0 and i % 5 > 0:
                self.fizzLock.acquire()
                printFizz()
                self.numLock.release()

    # printBuzz() outputs "buzz"

    def buzz(self, printBuzz):
        """
        :type printBuzz: method
        :rtype: void
        """
        for i in range(1, self.n+1):
            if i % 3 > 0 and i % 5 == 0:
                self.buzzLock.acquire()
                printBuzz()
                self.numLock.release()

    # printFizzBuzz() outputs "fizzbuzz"

    def fizzbuzz(self, printFizzBuzz):
        """
        :type printFizzBuzz: method
        :rtype: void
        """
        for i in range(1, self.n+1):
            if i % 3 == 0 and i % 5 == 0:
                self.fizzbuzzLock.acquire()
                printFizzBuzz()
                self.numLock.release()

    # printNumber(x) outputs "x", where x is an integer.

    def number(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1, self.n+1):
            self.numLock.acquire()
            if i % 3 == 0 and i % 5 == 0:
                self.fizzbuzzLock.release()
            elif i % 3 == 0:
                self.fizzLock.release()
            elif i % 5 == 0:
                self.buzzLock.release()
            else:
                printNumber(i)
                self.numLock.release()
