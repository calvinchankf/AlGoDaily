/*
    2nd approach: bfs
    - get the friend list for each friend
    - for each person, bfs to find all of his friends and put them into history
    - after finished one bfs, it means that we are done with one 'cluster'

    Time		O(NN) N: number of people
    Space		O(N)
    92 ms, faster than 46.85%
*/
var findCircleNum = function(M) {
    const n = M.length
    const seen = new Set()
    let res = 0
    for (let i = 0; i < n; i++) {
        if (bfs(M, i, seen) > 0) {
            res += 1
        }
    }
    return res
};

const bfs = (M, start, seen) => {
    let count = 0
    const q = [[start, start]]
    while (q.length > 0) {
        const [i, j] = q.shift()
        if (M[i][j] == 0) {
            continue
        }
        if (seen.has(j)) {
            continue
        }
        seen.add(j)
        count += 1
        for (let k = 0; k < M[j].length; k++) {
            q.push([j, k])
        }
    }
    return count
}