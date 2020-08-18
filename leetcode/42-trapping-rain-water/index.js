/*
    1st: min-max 2 arrays
    - similar to lc135, lc1493, lc915

    Time    O(3N)
    Space   O(2N)
    92 ms, faster than 41.18%
*/
var trap = function (heights) {
	const n = heights.length;
	const forwards = Array(n).fill(0);
	let fmax = 0;
	for (let i = 0; i < n; i++) {
		fmax = Math.max(fmax, heights[i]);
		forwards[i] = fmax;
	}

	const backwards = Array(n).fill(0);
	let bmax = 0;
	for (let i = n - 1; i >= 0; i--) {
		bmax = Math.max(bmax, heights[i]);
		backwards[i] = bmax;
	}

	let res = 0;
	for (let i = 0; i < n; i++) {
		res += Math.min(forwards[i], backwards[i]) - heights[i];
	}
	return res;
};
