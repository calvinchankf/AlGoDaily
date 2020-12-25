/*
    1st: BFS

    Time    O(N)
    Space   O(N)
    372 ms, faster than 100.00%
*/
var findNearestRightNode = function(root, u) {
    if (!root) {
        return null
    }
    const q = [root]
    while (q.length > 0) {
        const n = q.length
        let prev = null
        for (let i = 0; i < n; i++) {
            const node = q.shift()
            if (node == u) {
                return prev
            }
            prev = node
            if (node.right) {
                q.push(node.right)
            }
            if (node.left) {
                q.push(node.left)
            }
        }
    }
    return null
};