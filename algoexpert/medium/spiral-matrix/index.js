/*
    lc54
*/
function spiralTraverse(M) {
	// Write your code here.
	if (M.length === 0 || M[0].length === 0) {
		return [];
	}
	let top = 0;
	let right = M[0].length - 1;
	let bottom = M.length - 1;
	let left = 0;

	const res = [];

	while (top <= bottom && left <= right) {
		// go right
		for (let j = left; j <= right; j++) {
			res.push(M[top][j]);
		}
		top += 1;
		// go down
		for (let i = top; i <= bottom; i++) {
			res.push(M[i][right]);
		}
		right -= 1;
		// go left
		if (top <= bottom) {
			for (let j = right; j >= left; j--) {
				res.push(M[bottom][j]);
			}
			bottom -= 1;
		}
		// go up
		if (left <= right) {
			for (let i = bottom; i >= top; i--) {
				res.push(M[i][left]);
			}
			left += 1;
		}
	}
	return res;
}

// Do not edit the line below.
exports.spiralTraverse = spiralTraverse;
