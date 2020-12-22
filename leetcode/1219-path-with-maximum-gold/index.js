/*
    1st: backtracking
    - recursively traverse the matrix with dfs
    - to avoid redundant visiting:
        1. temporary put the candidate into the hashtable
        2. remove the candidate after the exploration
        This technique is known as backtacking
    - similar to lc51, 52

    Time    O(RRCC)
    Space   O(RC)
    544 ms, faster than 9.49%
*/
var getMaximumGold = function (grid) {
	const R = grid.length
    const C = grid[0].length
	let res = 0
    
    const backtrack = (i, j, total, seen) => {
        if (i < 0 || i == R || j < 0 || j == C) {
            return
        }
        if (grid[i][j] == 0) {
            return
        }
        const key = `${i},${j}`
        if (seen.has(key)) {
            return
        }
        seen.add(key)
        total += grid[i][j]
        res = Math.max(res, total)
        backtrack(i-1, j, total, seen)
        backtrack(i+1, j, total, seen)
        backtrack(i, j-1, total, seen)
        backtrack(i, j+1, total, seen)
        seen.delete(key)
    }
    
    for (let i = 0; i < R; i++) {
        for (let j = 0; j < C; j++) {
            backtrack(i, j, 0, new Set())
        }
    }
    
    return res
};
