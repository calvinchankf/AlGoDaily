/*
    1st approach: recursion
    - in each recursive function
        1. return the min and max node.val from the subtree
        2. compare the current node.val with the min and max which are from the return of subtrees

    Time    O(n)
    Space   O(h) h: height of the binary tree, worst case is O(n)
    92 ms, faster than 36.40%
*/
var maxAncestorDiff = function(root) {
    let res = 0
    const dfs = (node, parent) => {
        if (node == null) {
            return [parent.val, parent.val]
        }
        const [leftMin, leftMax] = dfs(node.left, node)
        const [rightMin, rightMax] = dfs(node.right, node)
        const curMin = Math.min(leftMin, rightMin)
        const curMax = Math.max(leftMax, rightMax)
        const a = Math.abs(curMin - node.val)
        const b = Math.abs(curMax - node.val)
        res = Math.max(res, a, b)
        return [
            Math.min(node.val, curMin),
            Math.max(node.val, curMax),
        ]
    }
    dfs(root)
    return res
};