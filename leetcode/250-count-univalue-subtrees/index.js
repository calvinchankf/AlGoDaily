/*
    recursion

    Time    O(N)
    Space   O(N)
    96 ms beats 44.33%
*/
var countUnivalSubtrees = function(root) {
    if (root == null) {
        return 0
    }
    const dfs = (node) => {
        if (node.left == null && node.right == null) {
            return [node.val, 1]
        }
        
        let left = node.val
        let leftCount = 0
        if (node.left) {
            [left, leftCount] = dfs(node.left)
        }
        
        let right = node.val
        let rightCount = 0
        if (node.right) {
            [right, rightCount] = dfs(node.right)
        }
        
        if (node.val == left && node.val == right) {
            return [node.val, leftCount + rightCount + 1]
        }
        return [null, leftCount + rightCount]
    }
    const [_, res] = dfs(root)
    return res
};