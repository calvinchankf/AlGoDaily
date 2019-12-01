from threading import Lock, Semaphore

"""
    1st: use Mutex Lock to deal with concurrency
    keep in mind: foo(), bar() will only be called once on each cooresponding thread
    36 ms, faster than 88.31%
"""


class FooBar(object):
    def __init__(self, n):
        self.n = n

        self.fooLock = Lock()
        self.barLock = Lock()

        self.barLock.acquire()

    def foo(self, printFoo):
        """
        :type printFoo: method
        :rtype: void
        """
        for i in range(self.n):
            self.fooLock.acquire()
            printFoo()
            self.barLock.release()

    def bar(self, printBar):
        """
        :type printBar: method
        :rtype: void
        """
        for i in range(self.n):
            self.barLock.acquire()
            printBar()
            self.fooLock.release()


"""
    2nd: use Semaphore to deal with concurrency

    keep in mind:
    - Semaphore(x) where x is capacity
    - semaphore.acquire() means locks -= 1
    - semaphore.release() means locks += 1

    44 ms, faster than 77.53%
"""


class FooBar(object):
    def __init__(self, n):
        self.n = n
        self.fooLock = Semaphore(1)
        self.barLock = Semaphore(0)

    def foo(self, printFoo):
        """
        :type printFoo: method
        :rtype: void
        """
        for _ in range(self.n):
            self.fooLock.acquire()
            printFoo()
            self.barLock.release()

    def bar(self, printBar):
        """
        :type printBar: method
        :rtype: void
        """
        for _ in range(self.n):
            self.barLock.acquire()
            printBar()
            self.fooLock.release()
