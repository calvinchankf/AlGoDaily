/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var sortList = function (head) {
	if (head == null || head.next == null) {
		return head;
	}
	let slow = head;
	let fast = head;
	while (fast.next !== null && fast.next.next !== null) {
		slow = slow.next;
		fast = fast.next.next;
	}
	const rightHalf = slow.next;
	slow.next = null;
	const left = sortList(head);
	const right = sortList(rightHalf);
	return merge(left, right);
};

const merge = (l1, l2) => {
	const dumpHead = new ListNode(0);
	let cur = dumpHead;
	let p1 = l1;
	let p2 = l2;
	while (p1 != null && p2 != null) {
		if (p1.val < p2.val) {
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
};
