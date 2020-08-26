function kadanesAlgorithm(array) {
	// Write your code here.
	let res = Number.MIN_SAFE_INTEGER;
	let cur = Number.MIN_SAFE_INTEGER;
	for (let x of array) {
		cur = Math.max(cur + x, x);
		res = Math.max(res, cur);
	}
	return res;
}

// Do not edit the line below.
exports.kadanesAlgorithm = kadanesAlgorithm;
