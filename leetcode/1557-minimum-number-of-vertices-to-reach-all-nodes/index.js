/*
    1st: indegree part of topo sort
    - basically the nodes with indegree == 0 are the starting points of the graph
    - this question assures that a solution exists, no need to check afterwards

    Time    O(V+E)
    Space   O(V+E)
    296 ms, faster than 100.00%
*/
var findSmallestSetOfVertices = function (n, edges) {
	const g = {};
	const indegrees = {};
	for (let i = 0; i < n; i++) {
		g[i] = [];
		indegrees[i] = 0;
	}
	for (let [prev, cur] of edges) {
		g[prev].push(cur);
		indegrees[cur] += 1;
	}
	const q = [];
	for (let key in indegrees) {
		if (indegrees[key] == 0) {
			q.push(key);
		}
	}
	return q;
};
