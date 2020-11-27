/*
    2nd: DFS preorder traversal, stack based, in-place
    - similar to lc114, 426, 430

    Time    O(N)
    Space   O(N) the stack
    80 ms, faster than 66.09%
*/
var flatten = function(head) {
    if (head == null) {
        return null
    }
    const dumphead = new Node()
    let prev = dumphead
    const stack = [head]
    while (stack.length > 0) {
        const node = stack.pop()
        node.prev = prev
        prev.next = node
        prev.child = null
        prev = node
        if (node.next) {
            stack.push(node.next)
        }
        if (node.child) {
            stack.push(node.child)
        }
    }
    // the catch: the first node.prev = null instead of dumphead
    dumphead.next.prev = null
    return dumphead.next
};