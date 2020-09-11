function reverseLinkedList(head) {
	// Write your code here.
	let cur = head;
	while (cur != null && cur.next != null) {
		const temp = cur.next;
		cur.next = cur.next.next;
		temp.next = head;
		head = temp;
	}
	return head;
}

// Do not edit the line below.
exports.reverseLinkedList = reverseLinkedList;
