/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/*
    1st approach: dfs all the nodes, and sum sup the values within the ranges

    Time    O(n)
    Space   O(h)
    268 ms, faster than 33.78%
*/
var rangeSumBST = function (root, L, R) {
	if (root == null || L > R) {
		return 0;
	}
	let res = 0;
	const q = [root];
	while (q.length > 0) {
		const node = q.shift();
		if (node.val >= L && node.val <= R) {
			res += node.val;
		}
		if (node.left) {
			q.push(node.left);
		}
		if (node.right) {
			q.push(node.right);
		}
	}
	return res;
};

/*
    2nd: optimize 1st
    - narrow down the range by comparing node.val >= L and node.val <= R

    Time    O(n)
    Space   O(h)
    224 ms, faster than 70.31% 
*/
var rangeSumBST = function(root, L, R) {
    if (root == null || L > R) {
        return 0
    }
    let res = 0
    const q = [root]
    while (q.length > 0) {
        const node = q.shift()
        if (node.val >= L && node.val <= R) {
            res += node.val
        }
        if (node.left && node.val >= L) {
            q.push(node.left)
        }
        if (node.right && node.val <= R) {
            q.push(node.right)
        }
    }
    return res
};