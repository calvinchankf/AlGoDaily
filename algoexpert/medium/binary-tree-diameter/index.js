// This is an input class. Do not edit.
class BinaryTree {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
  }
  
  function binaryTreeDiameter(tree) {
    let res = -1
    const dfs = (node) => {
        if (node == null) {
            return 0
        }
        const left = dfs(node.left)
        const right = dfs(node.right)
        res = Math.max(res, left + right)
        return Math.max(left, right) + 1
    }
    dfs(tree)
    return res
  }
  
  // Do not edit the line below.
  exports.binaryTreeDiameter = binaryTreeDiameter;
  exports.BinaryTree = BinaryTree;
  