// This is an input class. Do not edit.
class LinkedList {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

/*
    similar to lc19
*/
function removeKthNodeFromEnd(head, k) {
    const dumphead = new LinkedList()
    dumphead.next = head
    let slow = dumphead
    let fast = dumphead
    for (let i = 0; i <= k; i++) {
        fast = fast.next
    }
    if (fast == null) {
        head.value = head.next.value
        head.next = head.next.next
        return
    }
    while (fast != null) {
        fast = fast.next
        slow = slow.next
    }
    slow.next = slow.next.next
}

// Do not edit the line below.
exports.LinkedList = LinkedList;
exports.removeKthNodeFromEnd = removeKthNodeFromEnd;
