/*
    2nd: Floyd Warshall algorithm
    - similar to lc1462

    ref:
    - https://www.youtube.com/watch?v=4OQeCuLYj-4
    - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/discuss/490312/JavaC%2B%2BPython-Easy-Floyd-Algorithm
    - http://alrightchiu.github.io/SecondRound/all-pairs-shortest-pathfloyd-warshall-algorithm.html

    Time    O(N^3)
    Space   O(N^2)
    92 ms, faster than 98.46%
*/
var findTheCity = function (n, edges, distanceThreshold) {
	const dists = [];
	for (let i = 0; i < n; i++) {
		dists.push(Array(n).fill(Number.MAX_SAFE_INTEGER));
	}
	for (let [s, d, w] of edges) {
		dists[s][d] = w;
		dists[d][s] = w;
	}
	for (let i = 0; i < n; i++) {
		dists[i][i] = 0;
	}
	// see if node middle(k) can connect node i and node j
	// and update the cost if its smaller
	for (let k = 0; k < n; k++) {
		for (let i = 0; i < n; i++) {
			for (let j = 0; j < n; j++) {
				dists[i][j] = Math.min(dists[i][j], dists[i][k] + dists[k][j]);
			}
		}
	}
	let res = 0;
	let gCount = Number.MAX_SAFE_INTEGER;
	for (let i = 0; i < n; i++) {
		let count = 0;
		for (let j = 0; j < n; j++) {
			if (dists[i][j] <= distanceThreshold) {
				count += 1;
			}
		}
		if (count <= gCount) {
			gCount = count;
			res = i;
		}
	}
	return res;
};
