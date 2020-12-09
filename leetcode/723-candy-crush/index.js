/*
    2nd: simplify the logic in 1st
    - check cols using clone[i][j] == clone[i-1][j] == clone[i-2][j]
    - check rows using clone[i][j] == clone[i][j-1] == clone[i][j-2]
    - use lists to build the new board

    Time    O(kRC) worst case of k = 50/3
    Space   O(RC)
    220 ms, faster than 31.60%
*/
var candyCrush = function(board) {
    const R = board.length
    const C = board[0].length
    let clone = board
    while (true) {
        const toCollapse = new Set()
        for (let i = 0; i < R; i++) {
            for (let j = 0; j < C; j++) {
                if (clone[i][j] == 0) { continue }
                if (i-2 >= 0 && clone[i-1][j] == clone[i][j] && clone[i-2][j] == clone[i][j]) {
                    toCollapse.add(`${i},${j}`)
                    toCollapse.add(`${i-1},${j}`)
                    toCollapse.add(`${i-2},${j}`)
                }
                if (j-2 >= 0 && clone[i][j-1] == clone[i][j] && clone[i][j-2] == clone[i][j]) {
                    toCollapse.add(`${i},${j}`)
                    toCollapse.add(`${i},${j-1}`)
                    toCollapse.add(`${i},${j-2}`)
                }
            }
        }
        if (toCollapse.size == 0) { break }
        clone = buildBoard(clone, toCollapse)
    }
    return clone
};

const buildBoard = (board, toCollapse) => {
    const R = board.length
    const C = board[0].length
    const cols = []
    for (let j = 0; j < C; j++) {
        const col = []
        for (let i = R - 1; i >= 0; i--) {
            const key = `${i},${j}`
            if (toCollapse.has(key) == false) {
                col.push(board[i][j])
            }
        }
        cols.push(col)
    }
    const clone = []
    for (let i = 0; i < R; i++) {
        clone.push(Array(C).fill(0))
    }
    for (let j = 0; j < C; j++) {
        let i = R - 1
        const col = cols[j]
        while (col.length > 0) {
            clone[i][j] = col.shift()
            i -= 1
        }
    }
    return clone
}