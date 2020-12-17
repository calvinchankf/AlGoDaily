/*
    2nd: BFS + hashtable to avoid redundant revisit

    e.g. a/b = 2, b/c = 3
    means
    a -> b = 2
    b -> c = 3
    so, a -> b -> c = 2 * 3 = 6
    therefore, 
    we can start BFS from 1.0,
    after BFS, ratio = 1.0 * graph[a][b] * graph[b][c] = 1 * 2 * 3 = 6

    Time    O(N + QN) Q: number of queries, N: number of equations
    Space   O(Q+N)
    76 ms, faster than 75.12%
*/
var calcEquation = function(equations, values, queries) {
    const graph = {}
    for (let i = 0; i < equations.length; i++) {
        const [a, b] = equations[i]
        const ratio = values[i]
        
        if (a in graph === false) { graph[a] = {} }
        if (b in graph === false) { graph[b] = {} }
        
        graph[a][b] = ratio
        graph[b][a] = 1.0/ratio
    }
    
    const bfs = (src, dest) => {
        if (src in graph === false || dest in graph === false) {
            return -1
        }
        const seen = new Set()
        const q = [[src, 1.0]]
        while (q.length > 0) {
            const [node, r] = q.shift()
            if (node == dest) {
                return r
            }
            if (seen.has(node)) {
                continue
            }
            seen.add(node)
            if (node in graph == false) { continue }
            for (let nb in graph[node]) {
                q.push([nb, r * graph[node][nb]])
            }
        }
        return -1
    }
    
    const res = []
    for (let [s, e] of queries) {
        const r = bfs(s, e)
        res.push(r)
    }
    return res
};

/*
    followup: real time

    see ~/glassdoor/bloomberg/currency-exchange
*/