/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/*
    2nd approach
	1. bfs all the nodes, and put the node.val into a set
	2. if k-node.val exists in the set, return true immediately
    
	Time		O(n)
	Space		O(n) hashtable
	116 ms, faster than 58.28%
*/
var findTarget = function(root, k) {
    const hs = new Set()
    const q = [root]
    while (q.length > 0) {
        const node = q.shift()
        const remain = k - node.val
        if (hs.has(remain)) {
            return true
        }
        hs.add(node.val)
        if (node.left) {
            q.push(node.left)
        }
        if (node.right) {
            q.push(node.right)
        }
    }
    return false
};