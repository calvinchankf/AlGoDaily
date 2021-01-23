/*
    1st approach: bfs + hashtable + sort
    - similar to lc314
    this one is a bit annoying
    - basically, on the same row, we need to sort the nodes by values

    Time    O(NlogR)
    Space   O(N)
    84 ms, faster than 64.93%
*/
var verticalTraversal = function(root) {
    if (root == null) {
        return []
    }
    const ht = {}
    const q = [[root, 0]]
    let minCol = 0
    let maxCol = 0
    while (q.length > 0) {
        const columns = {}
        const n = q.length
        for (let i = 0; i < n; i++) {
            const [node, col] = q.shift()
            minCol = Math.min(minCol, col)
            maxCol = Math.max(maxCol, col)
            
            if (col in columns === false) {
                columns[col] = []
            }
            columns[col].push(node.val)
            
            if (node.left) {
                q.push([node.left, col-1])
            }
            if (node.right) {
                q.push([node.right, col+1])
            }
        }
        for (let key in columns) {
            const arr = columns[key]
            arr.sort((a, b) => a - b)
            if (key in ht === false) {
                ht[key] = []
            }
            ht[key] = ht[key].concat(arr)
        }
    }
    
    const res = []
    for (let i = minCol; i <= maxCol; i++) {
        res.push(ht[i])
    }
    
    return res
};
