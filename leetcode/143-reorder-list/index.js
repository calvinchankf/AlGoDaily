/*
    1st: 2 pointers
    - use some space

    Time    O(N)
    Space   O(N)
    116 ms, faster than 54.77% 
*/
var reorderList = function (head) {
	if (head == null) {
		return null;
	}
	const arr = [];
	let cur = head;
	while (cur != null) {
		arr.push(cur);
		cur = cur.next;
	}
	const dumpHead = new ListNode(-1);
	cur = dumpHead;
	let i = 0;
	let j = arr.length - 1;
	while (i < j) {
		cur.next = arr[i];
		cur = cur.next;
		i += 1;

		cur.next = arr[j];
		cur = cur.next;
		j -= 1;
	}
	cur.next = arr[i];
	cur = cur.next;
	cur.next = null;
	return dumpHead;
};

/*
    2nd:
    1. find the middlge point
    2. reverse the 2nd half
    3. merge 2 lists

    Time    O(N)
    Space   O(1)
    92 ms, faster than 95.77%
*/
var reorderList = function (head) {
	if (!head || !head.next) return;

	// find the middle point
	let slow = head;
	let fast = head;
	while (fast.next && fast.next.next) {
		slow = slow.next;
		fast = fast.next.next;
	}

	// split into two part head & part2
	let part2 = slow.next;
	slow.next = null;

	// reverse 2nd half
	let prev = null,
		cur = part2,
		next = cur.next;
	while (cur) {
		next = cur.next;
		cur.next = prev;
		prev = cur;
		cur = next;
	}

	part2 = prev;
	// merge head & part2
	while (head && part2) {
		let p1 = head.next;
		let p2 = part2.next;
		head.next = part2;
		head.next.next = p1;
		part2 = p2;
		head = p1;
	}

	return head;
};
