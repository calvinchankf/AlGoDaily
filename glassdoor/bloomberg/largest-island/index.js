/*
    https://leetcode.com/discuss/interview-experience/801398/bloomberg-software-engineer-new-grad-new-york-june-2020-offer

    You're given a 2-D grid of alphabets/letters in no specific order, 
    in the sense that the first row could contain the elements "a", "b", "b", "c", "z" and the second row could contain the elements: "a", "m", "p", "b", "g", and so on........ 
    You have to return which alphabet/letter occupies the largest 'chunk' of area.

    e.g.
    Input:
    [
        ["A", "B", "B", "C", "Z"],
        ["A", "M", "P", "B", "G"],
        ["A", "M", "M", "B", "G"],
        ["A", "A", "M", "B", "G"],
    ]

    Onput: A(which occupies 5 unit of area)
*/


/*
    questions:
    - upper/lower cases different?
    - 2 or more areas have the same size?
    - separate islands have the same alphabet letter?
*/
const largestIsland = (matrix) => {
    const ht = {}
    const seen = new Set()
    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[0].length; j++) {
            const key = `${i},${j}`
            if (seen.has(key)) {
                continue
            }
            const area = bfs(matrix, i, j, seen)
            const cell = matrix[i][j]
            if (cell in ht) {
                ht[cell] = Math.max(ht[cell], area)
            } else {
                ht[cell] = area
            }
        }
    }
    let islands = []
    let maxArea = 0
    for (let key in ht) {
        if (ht[key] > maxArea) {
            islands = [key]
            maxArea = ht[key]
        } else if (ht[key] == maxArea) {
            islands.push(key)
        }
    }
    return {islands, maxArea}
}

const bfs = (matrix, x, y, seen) => {
    let area = 0
    const q = [[x, y]]
    const cell = matrix[x][y]
    while (q.length > 0) {
        const [i, j] = q.shift()
        if (i < 0 || i == matrix.length || j < 0 || j == matrix[0].length) {
            continue
        }
        if (matrix[i][j] != cell) {
            continue
        }
        const key = `${i},${j}`
        if (seen.has(key)) {
            continue
        }
        seen.add(key)
        area += 1
        q.push([i-1, j])
        q.push([i+1, j])
        q.push([i, j-1])
        q.push([i, j+1])
    }
    return area
}

let a

a = [
    ["A", "B", "B", "C", "Z"],
    ["A", "M", "P", "B", "G"],
    ["A", "M", "M", "B", "G"],
    ["A", "A", "M", "B", "G"],
]
console.log(largestIsland(a))

a = [
    ["A", "B", "B", "C", "Z"],
    ["A", "M", "P", "B", "G"],
    ["A", "M", "P", "B", "G"],
    ["A", "M", "M", "B", "G"],
]
console.log(largestIsland(a))