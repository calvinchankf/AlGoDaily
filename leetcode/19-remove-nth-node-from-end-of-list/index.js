/*
    2 pointers

    Time    O(N)
    Space   O(1)
    76 ms, faster than 95.16%
*/
var removeNthFromEnd = function(head, n) {
    const dumphead = new ListNode()
	dumphead.next = head
	let slow = dumphead
	let fast = dumphead
	for (let i = 0; i < n; i++) {
		fast = fast.next
	}
	while (fast.next != null) {
        fast = fast.next
        slow = slow.next
	}
	slow.next = slow.next.next
	return dumphead.next
};