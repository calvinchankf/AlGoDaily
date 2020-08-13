/*
    Bellman Ford

    Time    O(VE)
    Space   O(V)
    136 ms, faster than 74.28%
*/
var networkDelayTime = function (times, N, K) {
	const dists = Array(N).fill(Number.MAX_SAFE_INTEGER);
	dists[K - 1] = 0;
	for (let i = 0; i < N; i++) {
		for (let [from, to, weight] of times) {
			from -= 1;
			to -= 1;
			const temp = dists[from] + weight;
			if (temp < dists[to]) {
				dists[to] = temp;
			}
		}
	}
	let maxDelay = 0;
	for (let d of dists) {
		if (d == Number.MAX_SAFE_INTEGER) {
			return -1;
		} else {
			maxDelay = Math.max(maxDelay, d);
		}
	}
	return maxDelay;
};
