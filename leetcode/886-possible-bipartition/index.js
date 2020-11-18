/*
    1st approach: BFS + nodes coloring
    - similar to lc785, 886

    idea learned from others:
    - https://www.youtube.com/watch?v=VlZiMD7Iby4

    Time    O(V+E)
    Space   O(V+E)
    572 ms, faster than 11.63%
*/
var possibleBipartition = function(N, dislikes) {
    const graph = {}
    for (let i = 1; i <= N; i++) {
        graph[i] = []
    }
    for (let [x, y] of dislikes) {
        graph[x].push(y)
        graph[y].push(x)
    }
    const cache = {}
    for (let i = 1; i <= N; i++) {
        if (i in cache === false) {
            if (bfs(graph, i, cache) === false) {
                return false
            }
        }
    }
    return true
};

const bfs = (graph, start, cache) => {
    const q = [[start, 1]]
    while (q.length > 0) {
        const [node, color] = q.shift()
        if (node in cache) {
            if (cache[node] != color) {
                return false
            }
            continue
        }
        cache[node] = color
        for (let nb of graph[node]) {
            q.push([nb, -color])
        }
    }
    return true
}