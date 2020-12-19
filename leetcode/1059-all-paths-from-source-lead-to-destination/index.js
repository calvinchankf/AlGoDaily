/*
    2nd: backtracking

    Time    O(E+V)
    Space   O(E+V)
    108 ms, faster than 84.21%
*/
var leadsToDestination = function(n, edges, source, destination) {
    const graph = {}
    for (let i = 0; i < n; i++) {
        graph[i] = []
    }
    for (let [s, d] of edges) {
        graph[s].push(d)
    }
    
    const backtrack = (node, seen) => {
        // base case
        if (graph[node].length === 0) {
            return node == destination
        }
        if (seen.has(node)) {
            return false
        }
        seen.add(node)
        for (let nb of graph[node]) {
            if (backtrack(nb, seen) === false) {
                return false
            }
        }
        seen.delete(node)
        return true
    }
    return backtrack(source, new Set())
};