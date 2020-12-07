/*
    2nd appraoch: Topological Ordering in BFS

    1. create a list to save to children for each node
    2. for each node, put the children in
        e.g. [4, 3], [1, 0], [5, 2], [5, 4], [5, 1], [2, 3]
        children list = [[], [0], [3], [], [3], [2,4,1]]
    3. count the indegrees for each node(indegrees = the number of incoming edges)
    4. put the nodes with 0 indegrees into a queue
    5. if the queue is not empty, append the dequeued node to the result and in the same time decrement it's children's indegrees
    6  after decrement, if there are nodes which has 0 indegrees, put them into the queue
    7. do 6) and 7) until the queue becomes empty
    8. need a 'cnt' to check if there is a cycle(for detail: see comment)

    Time    O(V+E)
    Space   O(V)
    76 ms, faster than 99.33%
*/
var findOrder = function(numCourses, prerequisites) {
    const n = numCourses
    const graph = []
    const indegrees = []
    for (let i = 0; i < n; i++) {
        graph.push([])
        indegrees.push(0)
    }
    for (let [dest, src] of prerequisites) {
        graph[src].push(dest)
        indegrees[dest] += 1
    }
    const q = []
    for (let i = 0; i < n; i++) {
        if (indegrees[i] == 0) {
            q.push(i)
        }
    }
    const res = []
    while (q.length > 0) {
        const node = q.shift()
        res.push(node)
        for (let child of graph[node]) {
            indegrees[child] -= 1
            if (indegrees[child] == 0) {
                q.push(child)
            }
        }
    }
    if (res.length != n) {
        return []
    }
    return res
};
