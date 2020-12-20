/*
    3rd approach
    - check every cell adjacent cells
    - for each cell, use binary digits to store the next status
    e.g.
    new status | old status
              0|0
              0|1
              1|0
              1|1
    - after calculation, shift the digit to the right to remove the old status

	Time	O(8RC + RC)
	Space	O(1)
	80 ms, faster than 64.89%
*/
var gameOfLife = function(board) {
    const R = board.length
    const C = board[0].length
    for (let i = 0; i < R; i++) {
        for (let j = 0; j < C; j++) {
            const count = countLivingNeighbors(board, i, j)
            if (board[i][j] % 10 == 1) {
                if (count == 2 || count == 3) {
                    board[i][j] += 10
                }
            } else {
                if (count == 3) {
                    board[i][j] += 10
                }
            }
        }
    }
    for (let i = 0; i < R; i++) {
        for (let j = 0; j < C; j++) {
            board[i][j] = board[i][j]/10
        }
    }
};

const countLivingNeighbors = (board, i, j) => {
    const R = board.length
    const C = board[0].length
    const dirs = [
        [-1, 0], [1, 0], [0, -1], [0, 1],
        [-1,-1], [-1,1], [1, 1], [1,-1]
    ]
    let count = 0
    for (let [di, dj] of dirs) {
        const _i = i + di
        const _j = j + dj
        if (_i < 0 || _i == R || _j < 0 || _j == C) {
            continue
        }
        if (board[_i][_j] % 10 == 1) {
            count += 1
        }
    }
    return count
}