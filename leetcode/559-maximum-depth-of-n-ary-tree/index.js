/*
    1st: iterative bfs
    
    Time    O(n)
    Space   O(h)
    100 ms, faster than 33.18%
*/
var maxDepth = function(root) {
    if (!root) {
        return 0
    }
    const q = [[root, 1]]
    let res = 0
    while (q.length > 0) {
        const [node, depth] = q.shift()
        res = Math.max(res, depth)
        for (let child of node.children) {
            q.push([child, depth + 1])
        }
    }
    return res
};

/*
    1st: recursive dfs

    Time    O(n)
    Space   O(h)
    92 ms, faster than 59.38%
*/
var maxDepth = function(root) {
    if (!root) {
        return 0
    }
    let maxD = 0
    for (let child of root.children) {
        const d = maxDepth(child)
        maxD = Math.max(maxD, d)
    }
    return maxD + 1
};