/*
    2 pointers
    - similar to lc287

    ref:
    - https://leetcode.com/articles/linked-list-cycle-ii/

    Time    O(N)
    Space   O(1)
    84 ms, faster than 32.43%
*/
var detectCycle = function (head) {
	if (head === null) {
		return null;
	}
	let slow = head;
	let fast = head;
	while (fast !== null && fast.next !== null) {
		slow = slow.next;
		fast = fast.next.next;
		if (slow === fast) {
			break;
		}
	}
	if (fast === null || fast.next === null) {
		return null;
	}
	slow = head;
	while (slow !== fast) {
		slow = slow.next;
		fast = fast.next;
	}
	return slow;
};
