/*
    2nd approach: bfs + hashtable
    - similar to lc987

    Time    O(N)
    Space   O(N)
    88 ms, faster than 67.26%
*/
var verticalOrder = function (root) {
    if (root == null) {
        return []
    }
    const ht = {}
    const q = [[root, 0]]
    let minCol = 0
    let maxCol = 0
    while (q.length > 0) {
        const [node, col] = q.shift()
        
        if (!(col in ht)) {
            ht[col] = []
        }
        ht[col].push(node.val)
        
        minCol = Math.min(minCol, col)
        maxCol = Math.max(maxCol, col)
        
        if (node.left) {
            q.push([node.left, col-1])
        }
        if (node.right) {
            q.push([node.right, col+1])
        }
    }
    
    const res = []
    for (let i = minCol; i <= maxCol; i++) {
        res.push(ht[i])
    }
    
    return res
};
