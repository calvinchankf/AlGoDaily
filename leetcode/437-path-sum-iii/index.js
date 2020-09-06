/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/*
    1st: hashtable
    - similar to lc325, 525, 930, 1124, 1171, 1546

    Time    O(N^2) in each recursion, we copy the while hashtable
    Space   O(N)
    340 ms, faster than 8.49%
*/
var pathSum = function (root, sum) {
	let res = 0;
	const dfs = (node, ht, total) => {
		if (node == null) {
			return;
		}
		const newTotal = total + node.val;

		if (newTotal == sum) {
			res += 1;
		}

		const remain = newTotal - sum;
		if (remain in ht) {
			res += ht[remain];
		}

		const newHt = { ...ht };
		if (newTotal in newHt) {
			newHt[newTotal] += 1;
		} else {
			newHt[newTotal] = 1;
		}

		dfs(node.left, newHt, newTotal);
		dfs(node.right, newHt, newTotal);
	};
	dfs(root, {}, 0);
	return res;
};
