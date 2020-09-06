/*
    2nd approach: same idea as 1st approach but shorter

	Time	O(l+r)
	Space	O(l+r) the result
    116 ms, faster than 97.26%
*/
var addTwoNumbers = function (l1, l2) {
	let carry = 0;
	const dumpHead = new ListNode(0);
	let cur = dumpHead;
	let cur1 = l1;
	let cur2 = l2;
	while (cur1 !== null || cur2 !== null) {
		let a = 0;
		if (cur1 != null) {
			a = cur1.val;
			cur1 = cur1.next;
		}

		let b = 0;
		if (cur2 != null) {
			b = cur2.val;
			cur2 = cur2.next;
		}

		const sum = a + b + carry;
		const val = sum % 10;
		carry = Math.floor(sum / 10);
		cur.next = new ListNode(val);
		cur = cur.next;
	}
	if (carry > 0) {
		cur.next = new ListNode(carry);
	}
	return dumpHead.next;
};
