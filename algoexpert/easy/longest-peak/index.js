/*
    min-max 2 arrays
*/
function longestPeak(array) {
	if (array.length < 3) {
		return 0;
	}
	// Write your code here.
	const n = array.length;
	const forwards = Array(n).fill(1);
	const backwards = Array(n).fill(1);
	for (let i = 1; i < n; i++) {
		if (array[i - 1] < array[i]) {
			forwards[i] = forwards[i - 1] + 1;
		}
	}
	for (let i = n - 2; i >= 0; i--) {
		if (array[i + 1] < array[i]) {
			backwards[i] = backwards[i + 1] + 1;
		}
	}
	let res = 0;
	for (let i = 1; i < n - 1; i++) {
		if (forwards[i] > forwards[i + 1] && backwards[i - 1] < backwards[i]) {
			const t = forwards[i] + backwards[i] - 1;
			if (t > res) {
				res = t;
			}
		}
	}
	return res;
}

// Do not edit the line below.
exports.longestPeak = longestPeak;
