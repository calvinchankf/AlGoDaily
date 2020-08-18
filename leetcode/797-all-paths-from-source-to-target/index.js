/*
    1st approach: BFS
    - since the question mentions that the graph is acyclic, we dont even need to worry if a node will be visited again in a cycle
    - therefore a simple BFS is good

    Time    O(n)
    Space   O(n)
    92 ms, faster than 52.48%
*/
var allPathsSourceTarget = function (graph) {
	const res = [];

	const q = [[0, []]];
	while (q.length > 0) {
		const [node, path] = q.shift();
		const newPath = [...path, node];
		if (node == graph.length - 1) {
			res.push(newPath);
			continue;
		}
		for (let child of graph[node]) {
			q.push([child, newPath]);
		}
	}

	return res;
};
/*
    2nd approach: DFS
    - since the question mentions that the graph is acyclic, we dont even need to worry if a node will be visited again in a cycle
    - therefore a simple DFS is good

    Time    O(n)
    Space   O(n)
    88 ms, faster than 87.93%
*/
var allPathsSourceTarget = function (graph) {
	const res = [];

	const dfs = (node, target, path) => {
		const newPath = [...path, node];
		if (node === target) {
			res.push(newPath);
			return;
		}
		for (let child of graph[node]) {
			dfs(child, target, newPath);
		}
	};
	dfs(0, graph.length - 1, []);

	return res;
};
