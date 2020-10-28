/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */


/*
    1st approach: bottom up recursive dfs

    Time    O(n)
    Space   O(h)
    92 ms, faster than 63.92%
*/
var findTilt = function(root) {
    if (!root) {
        return 0
    }
    return dfs(root)[0]
};

const dfs = (node) => {
    if (!node) {
        return [0, 0]
    }
    const [leftTile, leftSum] = dfs(node.left)
    const [rightTile, rightSum] = dfs(node.right)
    const tile = Math.abs(leftSum - rightSum)
    return [tile + leftTile + rightTile, node.val + leftSum + rightSum]
}