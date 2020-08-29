function topologicalSort(jobs, deps) {
	// Write your code here
	const jobSet = new Set(jobs);

	const g = {};
	const indegrees = {};

	for (let job of jobSet) {
		g[job] = [];
		indegrees[job] = 0;
	}

	for (let [prev, cur] of deps) {
		g[prev].push(cur);
		indegrees[cur] += 1;
	}

	const q = [];
	for (let job of jobSet) {
		if (indegrees[job] == 0) {
			q.push(job);
		}
	}

	const res = [];
	while (q.length > 0) {
		const node = q.shift();
		res.push(node);
		for (let child of g[node]) {
			indegrees[child] -= 1;
			if (indegrees[child] == 0) {
				q.push(child);
			}
		}
	}

	if (res.length != jobSet.size) {
		return "";
	}

	return res;
}

// Do not edit the line below.
exports.topologicalSort = topologicalSort;
