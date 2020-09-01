/*
    Merge two sorted linked lists and return it as a new list. 
    The new list should be made by splicing together the nodes of the first two lists.

    Time    O(A+B)
    Space   O(A+B)
    88 ms, faster than 69.63%
*/
var mergeTwoLists = function (l1, l2) {
	const dumpHead = new ListNode(0);
	let cur1 = l1;
	let cur2 = l2;
	let cur = dumpHead;
	while (cur1 !== null && cur2 !== null) {
		if (cur1.val < cur2.val) {
			cur.next = cur1;
			cur1 = cur1.next;
		} else {
			cur.next = cur2;
			cur2 = cur2.next;
		}
		cur = cur.next;
	}
	if (cur1 != null) {
		cur.next = cur1;
	}
	if (cur2 != null) {
		cur.next = cur2;
	}
	return dumpHead.next;
};
