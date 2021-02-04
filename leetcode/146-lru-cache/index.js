/*
    Doubly Linked List + Hashtable
    - similar to lc379, lc1429

    Time  put:O(1), get: O(1)
    196 ms, faster than 55.74%
*/
class DLLNode {
    constructor(key = -1, val = -1) {
        this.key = key
        this.val = val
        this.prev = null
        this.next = null
    }
}

class LRUCache {
    constructor(capacity = 0) {
        this.capacity = capacity
        this.ht = {}
        this.head = new DLLNode()
        this.tail = new DLLNode()
        this.head.next = this.tail
        this.tail.prev = this.head
        this.length = 0
    }
    _addToTail(node) {
        const last = this.tail.prev
        last.next = node
        node.prev = last
        node.next = this.tail
        this.tail.prev = node
    }
    _moveToTail(node) {
        node.prev.next = node.next
        node.next.prev = node.prev
        this._addToTail(node)
    }
    get(key) {
        if (key in this.ht == false) {
            return -1
        }
        const node = this.ht[key]
        this._moveToTail(node)
        return node.val
    }
    put(key, val) {
        if (key in this.ht == false) {
            const node = new DLLNode(key, val)
            this.ht[key] = node
            this._addToTail(node)
            this.length += 1
        } else {
            const node = this.ht[key]
            node.val = val
            this._moveToTail(node)
        }
        if (this.length > this.capacity) {
            const first = this.head.next
            first.prev.next = first.next
            first.next.prev = first.prev
            delete this.ht[first.key]
            this.length -= 1
        }
    }
}