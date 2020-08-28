/*
    BFS
*/
function minNumberOfJumps(array) {
	// Write your code here.
	const n = array.length;
	const q = [[0, 0]];
	while (q.length > 0) {
		const [node, steps] = q.shift();
		if (node == n - 1) {
			return steps;
		}
		if (node >= n) {
			continue;
		}
		const cands = array[node];
		for (let i = 1; i <= cands; i++) {
			q.push([node + i, steps + 1]);
		}
	}
	return -1;
}

// Do not edit the line below.
exports.minNumberOfJumps = minNumberOfJumps;
