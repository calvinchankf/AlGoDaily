/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/*
    2nd approach: iterative (reversed) inorder traversal

    Time    O(n)
    Space   O(h)
    76 ms, faster than 82.93%
*/
var bstToGst = function (root) {
	if (!root) {
        return null
    }
    let total = 0
    let cur = root
    const stack = []
    while (cur != null || stack.length > 0) {
        while (cur != null) {
            stack.push(cur)
            cur = cur.right
        }
        const node = stack.pop()
        total += node.val
        node.val = total
        cur = node.left
    }
    return root
};
