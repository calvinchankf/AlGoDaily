/*
    3rd: Bellman Ford
    - since we have a constraint that we can only traverse K stops,
        in each iteration, we should avoid updating the distances table directly

    Time    O(KE)
    Space   O(V)
    88 ms, faster than 87.63%
*/
var findCheapestPrice = function (n, flights, src, dst, K) {
	let dists = Array(n).fill(Number.MAX_SAFE_INTEGER);
	dists[src] = 0;
	for (let i = 0; i < K + 1; i++) {
		// avoid updating the distances table directly
		// because we want to make sure that in each iteration of i, we traverse 1 stop only
		const clone = [...dists];

		// normal bellman ford here
		for (let [from, to, weight] of flights) {
			const temp = dists[from] + weight;
			if (temp < clone[to]) {
				clone[to] = temp;
			}
		}

		// update the distances table
		dists = clone;
	}
	if (dists[dst] == Number.MAX_SAFE_INTEGER) {
		return -1;
	}
	return dists[dst];
};
