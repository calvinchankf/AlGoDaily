
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */


/*
    1st: recusion
    - similar to lc236, 1644, 1650, 1676

    Time    O(NK) N: size of the tree, K: nummber of 'nodes'
    Space   O(N)
    124 ms
*/
var lowestCommonAncestor = function(root, nodes) {
    if (root == null) { return null }
    let res = nodes[0]
    for (let i = 1; i < nodes.length; i++) {
        res = lca(root, res, nodes[i])
    }
    return res
};

const lca = (node, a, b) => {
    if (node === null || node === a || node === b) {
        return node
    }
    const left = lca(node.left, a, b)
    const right = lca(node.right, a, b)
    if (left !== null && right !== null) {
        return node
    }
    if (left != null) {
        return left
    }
    return right
}