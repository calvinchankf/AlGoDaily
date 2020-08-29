/*
    Time    O(N^2)
    Space   O(N^2)
    72 ms, faster than 69.32%
*/
var generateMatrix = function (n) {
	if (n <= 0) {
		return [];
	}

	const res = [];
	for (let i = 0; i < n; i++) {
		res.push(Array(n).fill(0));
	}

	let top = 0;
	let right = n - 1;
	let bottom = n - 1;
	let left = 0;
	let cur = 1;

	while (top <= bottom && left <= right) {
		for (let j = left; j <= right; j++) {
			res[top][j] = cur;
			cur += 1;
		}
		top += 1;
		// go down
		for (let i = top; i <= bottom; i++) {
			res[i][right] = cur;
			cur += 1;
		}
		right -= 1;
		// go left
		if (top <= bottom) {
			for (let j = right; j >= left; j--) {
				res[bottom][j] = cur;
				cur += 1;
			}
			bottom -= 1;
		}
		// go up
		if (left <= right) {
			for (let i = bottom; i >= top; i--) {
				res[i][left] = cur;
				cur += 1;
			}
			left += 1;
		}
	}
	return res;
};
