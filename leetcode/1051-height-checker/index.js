/**
 * @param {number[]} heights
 * @return {number}
 */
var heightChecker = function (heights) {
	const n = heights.length;
	const arr = [...heights];
	arr.sort((a, b) => a - b);
	let res = 0;
	for (let i = 0; i < n; i++) {
		if (heights[i] != arr[i]) {
			res += 1;
		}
	}
	return res;
};
