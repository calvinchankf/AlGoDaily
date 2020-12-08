/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/*
    1st: recursion, inorder traversal
    - similar to lc114, 426, 430, 897

    Time    O(N)
    Space   O(N)
    76 ms beats 77.57%
*/
var increasingBST = function(root) {
    const dumphead = new TreeNode()
    dumphead.right = root
    let prev = dumphead
    const inorder = (node) => {
        if (node == null) { return }
        
        inorder(node.left)
        
        const temp = node.right
        prev.left = null
        prev.right = node
        prev = node
        
        inorder(temp)
    }
    inorder(dumphead.right)
    
    prev.left = null
    return dumphead.right
};