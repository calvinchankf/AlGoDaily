"""
    Assume that you are designing a Browser history. 
    Say the user went into site "a" then "b" then "c". The history would be : a -> b -> c.
    Now assume you went into "a" again: The result becomes b -> c -> a.
    So the thing here is, if you revisit a site, you remove it from your result and so on.

    ref:
    - https://leetcode.com/discuss/interview-question/891632/bloomberg-onsite-video-interview-software-engineering-internship
"""


class ListNode(object):
    def __init__(self, url=''):
        self.url = url
        self.prev = None
        self.next = None


class BrowserHistory(object):
    def __init__(self):
        self.seen = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def visit(self, url):
        if url not in self.seen:
            self.seen[url] = ListNode(url)
            node = self.seen[url]
            self._addToTail(node)
        else:
            node = self.seen[url]
            self._moveToTail(node)

    def _addToTail(self, node):
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node

    def _moveToTail(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self._addToTail(node)

    def printHistory(self):
        res = []
        cur = self.head.next
        while cur != self.tail:
            res.append(cur.url)
            cur = cur.next
        print(res)


s = BrowserHistory()
s.visit('google.com')
s.visit('youtube.com')
s.visit('facebook.com')
s.printHistory()
s.visit('google.com')
s.printHistory()
s.visit('twitter.com')
s.printHistory()
