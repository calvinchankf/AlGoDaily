/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/*
    1st: recursive dfs

    Time    O(n)
    Space   O(h)
    88 ms, faster than 53.32%
*/
var maxDepth = function(root) {
    if (!root) {
        return 0
    }
    let left = maxDepth(root.left)
    let right = maxDepth(root.right)
    return Math.max(left, right) + 1
};

/*
    2nd: iterative bfs
    
    Time    O(n)
    Space   O(h)
    92ms, faster than 33.86%
*/
var maxDepth = function(root) {
    if (!root) {
        return 0
    }
    const q = [[root, 1]]
    let res = 0
    while (q.length > 0) {
        const [node, depth] = q.shift()
        res = Math.max(res, depth)
        if (node.left) {
            q.push([node.left, depth + 1])
        }
        if (node.right) {
            q.push([node.right, depth + 1])
        }
    }
    return res
};