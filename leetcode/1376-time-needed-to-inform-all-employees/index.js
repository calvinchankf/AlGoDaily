/*
    1st: hashtable + BFS
    - use a hashtable to store the edges
        e.g. {
            from1: [[to1, cost1], [to2, cost2],....]
            from2: [[to1, cost1], [to2, cost2],....]
            ...
        }
    - the result is the maxCost amongst the paths from root to each of the leaves

    Time    O(N + edges)
    Space   O(edges)
    344 ms, faster than 69.37%
*/
var numOfMinutes = function (n, headID, manager, informTime) {
	const graph = {};
	for (let i = 0; i < n; i++) {
		const supervisor = manager[i];
		if (supervisor in graph) {
			graph[supervisor].push(i);
		} else {
			graph[supervisor] = [i];
		}
	}
	let res = 0;
	const q = [[headID, 0]];
	while (q.length > 0) {
		const [node, t] = q.shift();
		res = Math.max(res, t);
		if (node in graph) {
			for (let child of graph[node]) {
				q.push([child, t + informTime[node]]);
			}
		}
	}
	return res;
};
