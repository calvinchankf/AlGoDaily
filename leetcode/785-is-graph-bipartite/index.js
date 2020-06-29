/*
    1st: dfs + hashtable
    - node coloring
    - see .idea.png

    Time    O(N)
    Space   O(N)
    76 ms, faster than 48.72%
*/
var isBipartite = function (graph) {
	const seen = {};
	// we need to check every node because it is possible that graph[0] doesn't have any vertices connected
	for (let i = 0; i < graph.length; i++) {
		if (!(i in seen)) {
			if (dfs(graph, i, 1, seen) == false) {
				return false;
			}
		}
	}
	return true;
};

const dfs = (graph, node, color, seen) => {
	if (node == null) {
		return true;
	}
	if (node in seen) {
		if (seen[node] != color) {
			return false;
		} else {
			return true;
		}
	}
	seen[node] = color;
	for (child of graph[node]) {
		if (dfs(graph, child, -color, seen) == false) {
			return false;
		}
	}
	return true;
};
