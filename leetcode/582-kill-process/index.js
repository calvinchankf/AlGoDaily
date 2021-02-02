/*
    1st approach: BFS + hashtable to avoid redundant visits

    Time    O(N)
    Space   O(H)
    336 ms, faster than 55.56%
*/
var killProcess = function(pid, ppid, kill) {
    const n = pid.length
    const graph = {}
    for (let i = 0; i < n; i++) {
        const node = pid[i]
        const parent = ppid[i]
        if (parent in graph === false) {
            graph[parent] = []
        }
        graph[parent].push(node)
    }
    const seen = new Set()
    const res = []
    const q = [kill]
    while (q.length > 0) {
        const node = q.shift()
        res.push(node)
        if (seen.has(node)) {
            continue
        }
        seen.add(node)
        if (node in graph) {
            for (let child of graph[node]) {
                q.push(child)
            }
        }
    }
    return res
};