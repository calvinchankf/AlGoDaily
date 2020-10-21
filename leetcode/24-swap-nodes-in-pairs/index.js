/*
    1st approach: iterative linked list traversal
	- one for the next
	- another one for the next.next
	- since we will change the head, we should use a dumphead

	Time	O(n)
	Space	O(1)
	0 ms, faster than 100.00%
*/
var swapPairs = function(head) {
    const dumphead = new ListNode(0)
    dumphead.next = head
    let cur = dumphead
    while (cur.next != null && cur.next.next != null) {
        const a = cur.next
        const b = cur.next.next
        const c = cur.next.next.next
        cur.next = b
        cur.next.next = a
        cur.next.next.next = c
        cur = cur.next.next
    }
    return dumphead.next
};