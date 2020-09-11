/*
    min-max 2 arrays

    Time    O(3N)
    Space   O(2N)
*/
function minRewards(scores) {
	// Write your code here.
	const n = scores.length;
	let forwards = Array(n).fill(1);
	let backwards = Array(n).fill(1);
	for (let i = 1; i < n; i++) {
		if (scores[i] > scores[i - 1]) {
			forwards[i] = forwards[i - 1] + 1;
		}
	}
	for (let i = n - 2; i >= 0; i--) {
		if (scores[i] > scores[i + 1]) {
			backwards[i] = backwards[i + 1] + 1;
		}
	}
	let res = 0;
	for (let i = 0; i < n; i++) {
		res += Math.max(forwards[i], backwards[i]);
	}
	return res;
}

// Do not edit the line below.
exports.minRewards = minRewards;
