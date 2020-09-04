/*
    1st approach:
    1. use a hashtable to map the address of each node and a new node
    2. iterate the linked list and construct a new linked list using the values in hashtable

    Time    O(2n)
    Space   O(n)
    96 ms, faster than 25.17%
*/
var copyRandomList = function (head) {
	const ht = new Map();
	let cur = head;
	while (cur !== null) {
		const clone = new Node(cur.val);
		ht.set(cur, clone);
		cur = cur.next;
	}
	cur = head;
	const cloneHead = new Node(0);
	let cloneCur = cloneHead;
	while (cur != null) {
		const node = ht.get(cur);
		if (cur.random) {
			node.random = ht.get(cur.random);
		}
		cloneCur.next = node;

		cur = cur.next;
		cloneCur = cloneCur.next;
	}
	return cloneHead.next;
};
