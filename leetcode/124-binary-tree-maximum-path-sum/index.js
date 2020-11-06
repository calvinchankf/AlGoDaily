/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/*
    1st approach: tree recursive dfs + kadan along each route 

    on each node, 

    the max value should be amongst
    - current node val
    - left branch sum + current node val
    - right branch sum + current node val
    - left branch sum + current node val + right branch sum

    since we only count branches' sum but not the total nodes' sum from each sub tree
    , we should just return the max amongst
    - current node val
    - left branch sum + current node val
    - right branch sum + current node val

    Time    O(n)
    Space   O(h)
    88 ms, faster than 94.83%
*/
var maxPathSum = function(root) {
    let res = -(2**31)
    const dfs = (node) => {
        if (node === null) {
            return 0
        }
        const left = dfs(node.left)
        const right = dfs(node.right)

        const mid = node.val
        const leftMid = node.val + left
        const midRight = node.val + right
        const leftMidRight = left + node.val + right

        // kadan's algorithm
        res = Math.max(res, mid, leftMid, midRight, leftMidRight)
        
        return Math.max(mid, leftMid, midRight)
    }
    dfs(root)
    
    return res
};