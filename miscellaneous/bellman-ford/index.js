/*
    1st: common Bellman Ford
    - Find the shortest path with negagtive weights
    - whereas dijkstra can only work on possitive weights

    ref:
    - https://www.youtube.com/watch?v=lyw4FaxrwHg

    e.g.
    - https://leetcode.com/problems/network-delay-time/

    Time    O(EV)
    Space   O(N)
*/
var bellmanFord = function (edges, N, src, dest) {
	const dists = Array(N).fill(Number.MAX_SAFE_INTEGER);
	dists[src - 1] = 0;
	for (let i = 0; i < N; i++) {
		for (let [from, to, weight] of edges) {
			from -= 1;
			to -= 1;
			const temp = dists[from] + weight;
			if (temp < dists[to]) {
				dists[to] = temp;
			}
		}
	}
	if (dists[dest] === Number.MAX_SAFE_INTEGER) {
		return -1;
	}
	return dists[dest];
};

/*
    2nd: Bellman Ford
    - within K steps

    ref:
    - https://www.youtube.com/watch?v=lyw4FaxrwHg

    e.g
    - https://leetcode.com/problems/cheapest-flights-within-k-stops/

    Time    O(EV)
    Space   O(N)
*/
var bellmanFord = function (edges, N, src, dest, K) {
	let dists = Array(N).fill(Number.MAX_SAFE_INTEGER);
	dists[src] = 0;
	for (let i = 0; i < K + 1; i++) {
		// avoid updating the distances table directly
		// because we want to make sure that in each iteration of i, we traverse 1 stop only
		const clone = [...dists];
		// normal bellman ford here
		for (let [from, to, weight] of edges) {
			const temp = dists[from] + weight;
			if (temp < clone[to]) {
				clone[to] = temp;
			}
		}
		// update the distances table
		dists = clone;
	}
	if (dists[dest] == Number.MAX_SAFE_INTEGER) {
		return -1;
	}
	return dists[dest];
};
