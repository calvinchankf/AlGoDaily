/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * 1st: 2 pointers
 *
 * Time     O(N)
 * Space    O(1)
 * 52ms beats 65.44%
 *
 * @param {ListNode} head
 * @return {ListNode}
 */
var middleNode = function (head) {
	let slow = head;
	let fast = head;
	while (fast != null && fast.next != null) {
		slow = slow.next;
		fast = fast.next.next;
	}
	return slow;
};
