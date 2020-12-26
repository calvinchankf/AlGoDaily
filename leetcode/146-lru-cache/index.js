/*
    Doubly Linked List + Hashtable
    - similar to lc379, lc1429

    Time  put:O(1), get: O(1)
    196 ms, faster than 55.74%
*/
class ListNode {
    constructor(key = -1, val = -1) {
        this.key = key
        this.val = val
        this.prev = null
        this.next = null   
    }
}
class LRUCache {
    constructor(capacity) {
        this.capacity = capacity
        this.map = {}
        this.listHead = new ListNode()
        this.listTail = new ListNode()
        this.listLength = 0
        this.listHead.next = this.listTail
        this.listTail.prev = this.listHead
    }
    get(key) {
        if (key in this.map) {
            this._moveToTail(this.map[key])
            return this.map[key].val
        }
        return -1
    }
    put(key, value) {
        let node = this.map[key]
        if (node == undefined) {
            node = new ListNode(key, value)
            this._addToTail(node)
            this.listLength += 1
        } else {
            node.val = value
            this._moveToTail(node)
        }
        this.map[key] = node
        if (this.listLength > this.capacity) {
            this._removeHead()
            this.listLength -= 1
        }
    }
    _addToTail(node) {
        let last = this.listTail.prev
        last.next = node
        node.prev = last
        node.next = this.listTail
        this.listTail.prev = node
    }
    _moveToTail(node) {
        node.prev.next = node.next
        node.next.prev = node.prev
        this._addToTail(node)
    }
    _removeHead() {
        let first = this.listHead.next
        this.listHead.next = first.next
        first.next.prev = this.listHead
        delete this.map[first.key]
    }
}