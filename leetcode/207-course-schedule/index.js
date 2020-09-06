/*
    2nd approach: topo ordering BFS but with hashtable

    Time    O(V+E)
    Space   O(V)
    92 ms, faster than 75.46%
*/
var canFinish = function (numCourses, prerequisites) {
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
		res.push(node);
		for (let nb of g[node]) {
			indegrees[nb] -= 1;
			if (indegrees[nb] == 0) {
				q.push(nb);
			}
		}
	}
	return res.length == n;
};
