/**
 * // Definition for a Node.
 * function Node(val, left, right) {
 *      this.val = val;
 *      this.left = left;
 *      this.right = right;
 *  };
 */

/*
    1st approach: straight forward intuition
    - put the nodes in an array in ascending order
    - update the values of the nodes

    Time    O(2n)
    Space   O(n)
    84 ms, faster than 51.14%
*/
var treeToDoublyList = function(root) {
    const nodes = []
    
    const inorder = (node) => {
        if (node == null) {
            return
        }
        inorder(node.left)
        nodes.push(node)
        inorder(node.right)
    }
    inorder(root)
    
    for (let i = 0; i < nodes.length; i++) {
        let left = null
        let right = null
        if (i == 0) {
            left = nodes[nodes.length-1]
        } else {
            left = nodes[i-1]
        }
        if (i+1 == nodes.length) {
            right = nodes[0]
        } else {
            right = nodes[i+1]
        }
        nodes[i].left = left
        nodes[i].right = right
    }
    
    return nodes[0]
};