/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/*
    3rd: bfs
    - traverse all the nodes in tree1 and tree2 and store them in 2 arrays
    - use a hashtable to do 2sum

    Time    O(2A+2B)
    Space   O(A+B)
    84 ms, faster than 46.15%
*/
var twoSumBSTs = function (root1, root2, target) {
	const hs = new Set();

	let q = [root1];
	while (q.length > 0) {
		const node = q.shift();
		hs.add(node.val);
		if (node.left) {
			q.push(node.left);
		}
		if (node.right) {
			q.push(node.right);
		}
	}

	q = [root2];
	while (q.length > 0) {
		const node = q.shift();

		if (hs.has(target - node.val)) {
			return true;
		}

		if (node.left) {
			q.push(node.left);
		}
		if (node.right) {
			q.push(node.right);
		}
	}

	return false;
};
