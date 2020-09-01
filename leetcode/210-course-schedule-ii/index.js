/*
    2nd appraoch: Topological Ordering in BFS

    1. create a list to save to children for each node
    2. for each node, put the children in
        e.g. [4, 3], [1, 0], [5, 2], [5, 4], [5, 1], [2, 3]
        children list = [[], [0], [3], [], [3], [2,4,1]]
    3. count the indegree for each node(indegree = the number of incoming edges)
    4. put the nodes with 0 indegree into a queue
    5. if the queue is not empty, append the dequeued node to the result and in the same time decrement it's children's indegree
    6  after decrement, if there are nodes which has 0 indegree, put them into the queue
    7. do 6) and 7) until the queue becomes empty
    8. need a 'cnt' to check if there is a cycle(for detail: see comment)

    Time    O(V+E)
    Space   O(V)
    76 ms, faster than 99.33%
*/
var findOrder = function (numCourses, prerequisites) {
	const n = numCourses;
	const g = {};
	const indegrees = {};
	for (let i = 0; i < n; i++) {
		g[i] = [];
		indegrees[i] = 0;
	}
	for (let [cur, prev] of prerequisites) {
		g[prev].push(cur);
		indegrees[cur] += 1;
	}
	const q = [];
	for (let key in indegrees) {
		if (indegrees[key] == 0) {
			q.push(key);
		}
	}
	const res = [];
	while (q.length > 0) {
		const node = q.shift();
		res.push(parseInt(node));
		for (let nb of g[node]) {
			indegrees[nb] -= 1;
			if (indegrees[nb] == 0) {
				q.push(nb);
			}
		}
	}
	if (numCourses !== res.length) {
		return [];
	}
	return res;
};
