/*
    1st approach: iterative bst traversal

    Time    O(height)
    Space   O(height)
    72 ms, faster than 56.73%
*/
var searchBST = function (root, target) {
	let cur = root;
	while (cur !== null) {
		if (target < cur.val) {
			cur = cur.left;
		} else if (target > cur.val) {
			cur = cur.right;
		} else {
			return cur;
		}
	}
	return null;
};
