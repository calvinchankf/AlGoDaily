/*
    3rd: iterative BST search

	Time		O(logn)
    Space	    O(height of the tree) the call stack
    104 ms, faster than 20.98%
*/
var closestValue = function (root, target) {
	let res = Number.MAX_SAFE_INTEGER;
	let cur = root;
	while (cur != null) {
		if (Math.abs(cur.val - target) < Math.abs(res - target)) {
			res = cur.val;
		}
		if (target < cur.val) {
			cur = cur.left;
		} else {
			cur = cur.right;
		}
	}
	return res;
};
