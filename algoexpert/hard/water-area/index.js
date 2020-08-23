function waterArea(heights) {
	// Write your code here.
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
}

// Do not edit the line below.
exports.waterArea = waterArea;
