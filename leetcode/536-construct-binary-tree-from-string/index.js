/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {string} s
 * @return {TreeNode}
 */
var str2tree = function(s) {
    const arr = []
    for (let c of s) {
        arr.push(c)
    }
    return dfs(arr)
};

const dfs = (arr) => {
    if (arr.length == 0) {
        return null
    }
    let s = ''
    while (arr.length > 0 && arr[0] != '(' && arr[0] != ")") {
        s += arr.shift()
    }
    const num = parseInt(s)
    const node = new TreeNode(num)
    
    if (arr.length > 0 && arr[0] == '(') {
        arr.shift()
        node.left = dfs(arr)
    }
    if (arr.length > 0 && arr[0] == '(') {
        arr.shift()
        node.right = dfs(arr)
    }
    if (arr.length > 0 && arr[0] == ')') {
        arr.shift()
    }
    return node
}