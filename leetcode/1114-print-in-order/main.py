from threading import Lock, Semaphore

"""
    python threading tutorial
    - https://www.laurentluce.com/posts/python-threads-synchronization-locks-rlocks-semaphores-conditions-events-and-queues/
"""


"""
    1st: use Mutex Lock to deal with concurrency
    20 ms, faster than 99.13%
"""


class Foo(object):
    def __init__(self):
        self.lock1 = Lock()
        self.lock2 = Lock()
        self.lock1.acquire()
        self.lock2.acquire()

    def first(self, printFirst):
        printFirst()
        self.lock1.release()

    def second(self, printSecond):
        self.lock1.acquire()
        printSecond()
        self.lock1.release()
        self.lock2.release()

    def third(self, printThird):
        self.lock2.acquire()
        printThird()
        self.lock2.release()


"""
    2nd approach: use Mutex Lock to deal with concurrency
    - use with to minimize the codebase
"""


class Foo(object):
    def __init__(self):
        self.lock1 = Lock()
        self.lock2 = Lock()
        self.lock1.acquire()
        self.lock2.acquire()

    def first(self, printFirst):
        printFirst()
        self.lock1.release()

    def second(self, printSecond):
        with self.lock1:
            printSecond()
            self.lock2.release()

    def third(self, printThird):
        with self.lock2:
            printThird()


"""
    3rd: use Semaphore to deal with concurrency

    keep in mind:
    - Semaphore(x) where x is capacity
    - semaphore.acquire() means locks -= 1
    - semaphore.release() means locks += 1
"""


class Foo(object):
    def __init__(self):
        self.two = Semaphore(0)
        self.three = Semaphore(0)

    def first(self, printFirst):
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.two.release()

    def second(self, printSecond):
        # printSecond() outputs "second". Do not change or remove this line.
        with self.two:
            printSecond()
            self.three.release()

    def third(self, printThird):
        # printThird() outputs "third". Do not change or remove this line.
        with self.three:
            printThird()
