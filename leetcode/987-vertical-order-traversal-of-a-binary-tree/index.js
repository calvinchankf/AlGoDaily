/*
    1st approach: bfs + hashtable + sort
    - similar to lc314
    this one is a bit annoying
    - basically, on the same row, we need to sort the nodes by values

    Time    O(NlogR)
    Space   O(N)
    84 ms, faster than 64.93%
*/
var verticalTraversal = function (root) {
	if (root == null) {
        return []
    }
    const ht = {}
    const q = [[root, 0]]
    let minCol = 0
    let maxCol = 0
    while (q.length > 0) {
        const n = q.length
        const columns = {}
        for (let i = 0; i < n; i++) {
            const [node, col] = q.shift()
        
            if ((col in columns) === false) {
                columns[col] = []
            }
            columns[col].push(node.val)

            minCol = Math.min(minCol, col)
            maxCol = Math.max(maxCol, col)

            if (node.left) {
                q.push([node.left, col-1])
            }
            if (node.right) {
                q.push([node.right, col+1])
            }
        }
        for (let col in columns) {
            if ((col in ht)  === false) {
                ht[col] = []
            }
            const x = columns[col].sort((a, b) => a - b)
            ht[col] = ht[col].concat(x)
        }
        
    }
    
    const res = []
    for (let i = minCol; i <= maxCol; i++) {
        res.push(ht[i])
    }
    
    return res
};
