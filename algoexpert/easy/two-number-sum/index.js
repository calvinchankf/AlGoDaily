function twoNumberSum(array, targetSum) {
	// Write your code here.
	const ht = new Set();
	for (let x of array) {
		const target = targetSum - x;
		if (ht.has(target)) {
			return [target, x];
		}
		ht.add(x);
	}
	return [];
}

// Do not edit the line below.
exports.twoNumberSum = twoNumberSum;
