// This is an input class. Do not edit.
class LinkedList {
	constructor(value) {
		this.value = value;
		this.next = null;
	}
}

function findLoop(head) {
	if (head === null) {
		return null;
	}
	// Write your code here.
	let slow = head;
	let fast = head;
	while (fast !== null && fast.next !== null) {
		slow = slow.next;
		fast = fast.next.next;
		if (slow == fast) {
			break;
		}
	}
	if (fast == null || fast.next == null) {
		return null;
	}
	slow = head;
	while (slow != fast) {
		slow = slow.next;
		fast = fast.next;
	}
	return slow;
}

// Do not edit the lines below.
exports.LinkedList = LinkedList;
exports.findLoop = findLoop;
