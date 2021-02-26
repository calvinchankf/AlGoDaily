/*
    2nd: BFS + hashing
    - if 2 islands have the same shape, their nodes traversal order must be the same
    - so we can record the traversal direction as a hash, and use a hashtable to deduplicate the islands

    Time    O(RC)
    Space   O(RC)
    112 ms, faster than 67.72%
*/
var numDistinctIslands = function(grid) {
    if (grid.length == 0 || grid[0].length == 0) {
        return 0
    }
    const R = grid.length 
    const C = grid[0].length
    const seen = new Set()
    const res = new Set()
    for (let i = 0; i < R; i++) {
        for (let j = 0; j < C; j++) {
            const key = `${i},${j}`
            if (grid[i][j] == 1 && seen.has(key) === false) {
                const pattern = bfs(grid, i, j, seen)
                res.add(pattern)
            }
        }
    }
    return res.size
};

const bfs = (grid, x, y, seen) => {
    const R = grid.length 
    const C = grid[0].length
    
    const q = [[x, y]]
    const path = []
    
    while (q.length > 0) {
        const [i, j] = q.shift()
        
        if (i < 0 || i == R || j < 0 || j == C) {
            continue
        }
        if (grid[i][j] != 1) {
            continue
        }
        
        const key = `${i},${j}`
        if (seen.has(key)) {
            continue
        }
        seen.add(key)
        path.push(`${i-x},${j-y}`)
        
        q.push([i-1, j])
        q.push([i+1, j])
        q.push([i, j-1])
        q.push([i, j+1])
    }
    return path.join('-')
}