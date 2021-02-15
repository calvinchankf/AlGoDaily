"""
    The first customer
    - https://www.1point3acres.com/bbs/thread-711101-1-1.html
    - https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=669432&ctid=230591

    Write a restaurant table waiting system. Given a list of info of a diners, and K, 
    return the first customer the restaurant should serve

    e.g.
    [   
        {name: dog, size: 4, waittime: 150}, 
        {name: cat, size: 2, waittime: 200},
        {name: bird, size: 3, waittime: 300},
    ]

    if K = 3, return 'cat'
    if K = 4, return 'dog'
"""


class Customer:
    def __init__(self, name='', size=2**32, waitTime=0):
        self.name = name
        self.size = size
        self.waitTime = waitTime


class WaitingQueue:
    def __init__(self):
        self.customers = []

    def lineUp(self, customer):
        self.customers.append(customer)

    def letCustomerIn(self, k):
        targetIdx = -1
        for i in range(len(self.customers)):
            if self.customers[i].size <= k:
                targetIdx = i
                break
        if targetIdx == -1:
            return None
        return self.customers.pop(targetIdx)


wq = WaitingQueue()
wq.lineUp(Customer('dog', 4, 150))
wq.lineUp(Customer('cat', 2, 200))
wq.lineUp(Customer('bird', 3, 300))
# print(wq.letCustomerIn(3).name)
assert wq.letCustomerIn(3).name == 'cat'
# print(wq.letCustomerIn(4).name)
assert wq.letCustomerIn(4).name == 'dog'

print("-----")

"""
    variation: The last customer
    https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=595512&ctid=230591

    e.g.
    [   
        {name: dog, size: 4, waittime: 150}, 
        {name: cat, size: 2, waittime: 200},
        {name: bird, size: 3, waittime: 300},
        {name: rat, size: 7, waittime: 400},
    ]

    if K = 3, return 'cat'
    if K = 5, return 'rat'
"""


def getFirstCustomer(customers, k):
    res = None
    customers.sort(key=lambda x: x.waitTime)
    for i in range(len(customers)):
        if customers[i].size <= k:
            res = customers[i]
    return res


a = [
    Customer('dog', 4, 150),
    Customer('cat', 2, 200),
    Customer('bird', 3, 300),
    Customer('rat', 7, 400),
]
b = 3
print(getFirstCustomer(a, 3).name)

a = [
    Customer('dog', 4, 150),
    Customer('cat', 2, 200),
    Customer('bird', 3, 300),
    Customer('rat', 4, 700),
]
b = 4
print(getFirstCustomer(a, 4).name)

print("-----")

"""
    variation: for small restaurants, find the group just fit

    e.g.
    [   
        {name: dog, size: 4, waittime: 150}, 
        {name: cat, size: 2, waittime: 200},
        {name: bird, size: 3, waittime: 300},
    ]

    if K = 5, return None
    if K = 3, return 'bird'
    if K = 3, return None
    if K = 4, return 'dog'
    if K = 2, return 'cat'
"""


class WaitingQueue:
    def __init__(self):
        self.queues = {}

    def lineUp(self, customer):
        size = customer.size
        if size not in self.queues:
            self.queues[size] = []
        self.queues[size].append(customer)

    def letCustomerIn(self, K):
        if K not in self.queues or len(self.queues[K]) == 0:
            return None
        return self.queues[K].pop(0)


wq = WaitingQueue()
wq.lineUp(Customer('dog', 4, 150))
wq.lineUp(Customer('cat', 2, 200))
wq.lineUp(Customer('bird', 3, 300))
print(wq.letCustomerIn(5))
assert wq.letCustomerIn(5) == None
print(wq.letCustomerIn(3).name)
print(wq.letCustomerIn(3))
assert wq.letCustomerIn(3) == None
print(wq.letCustomerIn(4).name)
print(wq.letCustomerIn(2).name)
