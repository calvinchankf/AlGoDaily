/*
    1st approach: recursion
    - for each node, if depths from left and right diff > 1, it is unbalanced

    Time    O(n)
    Space   O(n)
    88 ms, faster than 84.62%
*/
var isBalanced = function(root) {
    return dfs(root) != -1
};

const dfs = (node) => {
    if (node == null) {
        return 0
    }
    const left = dfs(node.left)
    const right = dfs(node.right)
    if (left == -1 || right == -1) {
        return -1
    }
    const diff = Math.abs(left - right)
    if (diff > 1) {
        return -1
    }
    // the height of a subtree is the max depth from either left or right child
    return Math.max(left, right) + 1
}