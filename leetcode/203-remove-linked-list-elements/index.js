/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */

/*
    1st approach
    - remove the next pointer if it contains the target in a loop

    Time    (n)
    Space   O(1)
    100 ms, faster than 31.94%
*/
var removeElements = function (head, val) {
	let dumb = new ListNode(0);
	dumb.next = head;
	let cur = dumb;
	while (cur !== null) {
		while (cur.next !== null && cur.next.val == val) {
			cur.next = cur.next.next;
		}
		cur = cur.next;
	}
	return dumb.next;
};
