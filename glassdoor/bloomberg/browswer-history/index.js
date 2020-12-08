/*
    Assume that you are designing a Browser history. 
    Say the user went into site "a" then "b" then "c". The history would be : a -> b -> c.
    Now assume you went into "a" again: The result becomes b -> c -> a.
    So the thing here is, if you revisit a site, you remove it from your result and so on.

    ref:
    - https://leetcode.com/discuss/interview-question/891632/bloomberg-onsite-video-interview-software-engineering-internship
*/
class DLLNode {
    constructor(url = '') {
        this.url = url
        this.prev = null
        this.next = null
    }
}

class BrowserHistory {
    constructor() {
        this.ht = {}
        this.head = new DLLNode()
        this.tail = new DLLNode()
        this.head.next = this.tail
        this.tail.prev = this.head
    }
    _removeNode(node) {
        node.prev.next = node.next
        node.next.prev = node.prev
    }
    _addToTail(node) {
        const last = this.tail.prev
        node.prev = last
        node.next = this.tail
        last.next = node
        this.tail.prev = node
    }
    visit(url) {
        let node
        if (url in this.ht) {
            node = this.ht[url]
            this._removeNode(node)
        } else {
            node = new DLLNode(url)
            this.ht[url] = node
        }
        this._addToTail(node)
    }
    printHistory() {
        const history = []
        let cur = this.head.next
        while (cur != this.tail) {
            history.push(cur.url)
            cur = cur.next
        }
        console.log(history)
    }
}

s = new BrowserHistory()
s.visit('google.com')
s.visit('youtube.com')
s.visit('facebook.com')
s.printHistory()
s.visit('google.com')
s.printHistory()
s.visit('twitter.com')
s.printHistory()