// This is an input class. Do not edit.
class LinkedList {
	constructor(value) {
		this.value = value;
		this.next = null;
	}
}

function mergeLinkedLists(headOne, headTwo) {
	// Write your code here.
	const dumpHead = new LinkedList(-1);
	let cur = dumpHead;
	let p1 = headOne;
	let p2 = headTwo;
	while (p1 != null && p2 != null) {
		if (p1.value < p2.value) {
			cur.next = p1;
			p1 = p1.next;
		} else {
			cur.next = p2;
			p2 = p2.next;
		}
		cur = cur.next;
	}
	if (p1 != null) {
		cur.next = p1;
	}
	if (p2 != null) {
		cur.next = p2;
	}
	return dumpHead.next;
}

// Do not edit the line below.
exports.LinkedList = LinkedList;
exports.mergeLinkedLists = mergeLinkedLists;
