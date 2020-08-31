var topoSort = function (n, prerequisites) {
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
	return res;
};

var a;

a = 6;
b = [
	[3, 4],
	[0, 1],
	[2, 5],
	[4, 5],
	[1, 5],
	[3, 2],
];
console.log(topoSort(a, b));

a = 6;
b = [
	[3, 4],
	[0, 1],
	[2, 5],
	[4, 5],
	[1, 5],
	[3, 2],
	[5, 3],
];
console.log(topoSort(a, b));
