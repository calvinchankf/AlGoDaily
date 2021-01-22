/*
    1st approach: BFS + hastable
    - similar to lc286: walls and gates
    - on each cell
        - sum up all the steps from each buildings
        - record the number of buildings which can access this cell
    - find the min

    Time    O(kRRCC) k: number of buildings
    Space   O(2RC)
    348 ms, faster than 46.81% 
*/
var shortestDistance = function(grid) {
    if (grid.length == 0 || grid[0].length == 0) {
        return -1
    }
    const R = grid.length
    const C = grid[0].length
    const dists = []
    const visitCounts = []
    for (let i = 0; i < R; i++) {
        dists.push(Array(C).fill(0))
        visitCounts.push(Array(C).fill(0))
    }
    let buildingCount = 0
    for (let i = 0; i < R; i++) {
        for (let j = 0; j < C; j++) {
            if (grid[i][j] == 1) {
                buildingCount += 1
                bfs(grid, i, j, dists, visitCounts)
            }
        }
    }
    let res = 2**32
    for (let i = 0; i < R; i++) {
        for (let j = 0; j < C; j++) {
            if (grid[i][j] == 0 && visitCounts[i][j] == buildingCount) {
                res = Math.min(res, dists[i][j])
            }
        }
    }
    if (res == 2**32) { return -1 }
    return res
};

const bfs = (grid, x, y, dists, visitCounts) => {
    const R = grid.length
    const C = grid[0].length
    const q = [[x, y, 0]]
    const seen = new Set()
    while (q.length > 0) {
        const [i, j, steps] = q.shift()
        if (i < 0 || i == R || j < 0 || j == C) {
            continue
        }
        const key = `${i},${j}`
        if (seen.has(key)) {
            continue
        }
        seen.add(key)
        if (grid[i][j] == 0 || (i == x && j == y)) {
            dists[i][j] += steps
            visitCounts[i][j] += 1
            q.push([i-1, j, steps + 1])
            q.push([i+1, j, steps + 1])
            q.push([i, j-1, steps + 1])
            q.push([i, j+1, steps + 1])
        }
    }
}