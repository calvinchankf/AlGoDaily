var hasCycle = function (head) {
	let slow = head;
	let fast = head;
	while (fast !== null && fast.next !== null) {
		slow = slow.next;
		fast = fast.next.next;
		if (slow === fast) {
			return true;
		}
	}
	return false;
};
