/*
    1st: linked list traversal

    Time    O(N)
    Space   O(N)
    64 ms, faster than 100.00%
*/
var deleteNodes = function (head, m, n) {
	const dumpHead = new ListNode();
	dumpHead.next = head;
	let cur = dumpHead;
	let i = 0;
	while (cur.next !== null) {
		cur = cur.next;
		i += 1;
		if (i == m) {
			let j = 0;
			let temp = cur;
			while (j < n && temp !== null) {
				temp = temp.next;
				j += 1;
				if (temp != null) {
					cur.next = temp.next;
				} else {
					cur.next = null;
				}
				i = 0;
			}
		}
	}
	return dumpHead.next;
};
