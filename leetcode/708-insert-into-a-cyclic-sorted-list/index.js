/*
    2nd approach: optimize the above approach
    - find the minNode
    - there are 2 cases to insert a node
        1. cur <= target < cur.next
        2. cur.next == head and insertion no yet happen

    Time    O(2N)
    Space   O(1)
    92 ms, faster than 27.43%
*/
var insert = function(head, insertVal) {
    if (head == null) {
        const node = new Node(insertVal)
        node.next = node
        return node
    }
    // find the min node
    let minNode = head
    let cur = head
    while (true) {
        cur = cur.next
        if (cur.val < minNode.val) {
            minNode = cur
        }
        if (cur === head) {
            break
        }
    }
    // start from min node
    cur = minNode
    while (true) {
        if (cur.val <= insertVal && cur.next.val > insertVal) {
            const node = new Node(insertVal)
            node.next = cur.next
            cur.next = node
            break
        }
        if (cur.next == minNode) {
            const node = new Node(insertVal)
            node.next = cur.next
            cur.next = node
            break
        }
        cur = cur.next
    }
    return head
};