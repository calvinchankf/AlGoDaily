/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/*
    1st approach: bottom-up recursive dfs

    Time    O(n)
    Space   O(h)
    20 ms, faster than 58.34%
*/
var isUnivalTree = function(root) {
    if (!root) {
        return true
    }
    if (isUnivalTree(root.left) == false) {
        return false
    }
    if (isUnivalTree(root.right) == false) {
        return false
    }
    
    const hs = new Set()
    if (root.left) {
        hs.add(root.left.val)
    }
    if (root.right) {
        hs.add(root.right.val)
    }
    hs.add(root.val)
    return hs.size == 1
};

/*
    3rd approach: bfs

    Time    O(n)
    Space   O(w)
    20 ms, faster than 58.34%
*/
var isUnivalTree = function(root) {
    if (!root) {
        return true
    }
    const cur = root.val
    const q = [root]
    while (q.length > 0) {
        const node = q.shift()
        if (node.val != cur) {
            return false
        }
        if (node.left) {
            q.push(node.left)
        }
        if (node.right) {
            q.push(node.right)
        }
    }
    return true
};