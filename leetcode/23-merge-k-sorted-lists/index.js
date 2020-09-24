/*
    2nd approach: reuse the sorted 2 lists

    Time    O(nk)
    Space   O(nk)
	296 ms, faster than 40.40%
*/
var mergeKLists = function (lists) {
	const dumpHead = new ListNode(0);
	for (let x of lists) {
		dumpHead.next = mergeTwoLists(dumpHead.next, x);
	}
	return dumpHead.next;
};

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
