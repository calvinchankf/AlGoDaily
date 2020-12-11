/*
    Iterative Inorder Traversal of BST

    Time of next()      O(H)
    Time of hasNext()   O(1)
    Space               O(H)  
    140 ms, faster than 93.28%
*/
class BSTIterator {
    constructor(root) {
        this.stack = []
        this.cur = root
    }
    next() {
        while (this.cur != null) {
            this.stack.push(this.cur)
            this.cur = this.cur.left
        }
        const node = this.stack.pop()
        const res = node.val
        this.cur = node.right
        return res
    }
    hasNext() {
        return this.stack.length > 0 || this.cur != null
    }
}