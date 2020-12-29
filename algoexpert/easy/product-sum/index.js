// Tip: You can use the Array.isArray function to check whether an item
// is a list or an integer.
function productSum(array) {
	// Write your code here.
	const f = (arr, level) => {
		let sum = 0;
		for (let x of arr) {
			if (Array.isArray(x)) {
				sum += level * f(x, level + 1);
			} else {
				sum += x;
			}
		}
		return sum;
	};
	return f(array, 2);
}

// Do not edit the line below.
exports.productSum = productSum;
