class TreeNode {
    constructor(val) {
        this.val = val
        this.left = this.right = null;
    }
}

/*
    easy approach: similar to lc536, 572, 606
    e.g. 1(2()())(3(4()())(5()()))

    Time    O(n)
    Space   O(h)
    924 ms, faster than 5.02%
*/

var serialize = function(root) {
    if (root == null) {
        return ''
    }
    const left = serialize(root.left)
    const right = serialize(root.right)
    return `${root.val}(${left})(${right})`
};

var deserialize = function(data) {
    const q = []
    for (let c of data) {
        q.push(c)
    }
    return dfs(q)
};

const dfs = (q) => {
    if (q.length == 0) {
        return null
    }
    let numStr = ''
    while (q.length > 0 && q[0] != '(' && q[0] != ')') {
        numStr += q.shift()
    }
    let node = null
    if (numStr.length > 0) {
        const num = parseInt(numStr)
        node = new TreeNode(num)
    }
    // left child
    if (q.length > 0 && q[0] == '(') {
        q.shift()
        node.left = dfs(q)
    }
    // right child
    if (q.length > 0 && q[0] == '(') {
        q.shift()
        node.right = dfs(q)
    }
    // end
    if (q.length > 0 && q[0] == ')') {
        q.shift()
    }
    return node
}