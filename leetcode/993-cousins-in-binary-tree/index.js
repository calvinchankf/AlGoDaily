/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/*
    1st approach: BFS + hashtable
    - BFS the tree level by level
    - use a hashtable to store [parent, currentnode]
    - after we have done the iterating one level, check if the x, y are on the same level and have diff parents

    Time    O(n)
    Space   O(n)
    12ms beats 100%
*/
var isCousins = function (root, x, y) {
	let xParent = null;
	let xDepth = -1;
	let yParent = null;
	let yDepth = -1;

	let q = [[root, null, 0]];
	while (q.length > 0) {
		const [node, parent, depth] = q.pop(0);
		if (node.val == x) {
			xParent = parent;
			xDepth = depth;
		}
		if (node.val == y) {
			yParent = parent;
			yDepth = depth;
		}
		if (node.left) {
			q.push([node.left, node, depth + 1]);
		}
		if (node.right) {
			q.push([node.right, node, depth + 1]);
		}
	}
	return xDepth == yDepth && xParent != yParent;
};
