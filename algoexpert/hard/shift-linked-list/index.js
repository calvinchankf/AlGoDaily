function shiftLinkedList(head, k) {
	// Write your code here.
	let n = 0;
	let cur = head;
	let tail = null;
	while (cur !== null) {
		tail = cur;
		cur = cur.next;
		n += 1;
	}
	k = ((k % n) + n) % n;
	if (k == 0) {
		return head;
	}

	const dumpHead = new LinkedList(-1);
	dumpHead.next = head;

	let diff = n - k;
	cur = dumpHead;
	while (diff > 0) {
		cur = cur.next;
		diff -= 1;
	}
	// console.log('yo', cur)
	const secondHalf = cur.next;
	cur.next = null;
	tail.next = head;
	// dumpHead.next = secondHalf
	return secondHalf;
}

// This is the class of the input linked list.
class LinkedList {
	constructor(value) {
		this.value = value;
		this.next = null;
	}
}

// Do not edit the line below.
exports.shiftLinkedList = shiftLinkedList;
