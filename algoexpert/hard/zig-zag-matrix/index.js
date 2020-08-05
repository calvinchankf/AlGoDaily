/*
    lc498
*/
function zigzagTraverse(M) {
	// Write your code here.
	const R = M.length;
	const C = M[0].length;
	const res = [];
	for (let i = 0; i < R; i++) {
		let arr = [];
		let i_ = i;
		let j = 0;
		while (i_ >= 0 && j < C) {
			arr.push(M[i_][j]);
			i_ -= 1;
			j += 1;
		}
		res.push(arr);
	}
	for (let j = 1; j < C; j++) {
		let arr = [];
		let i = R - 1;
		let j_ = j;
		while (i >= 0 && j_ < C) {
			arr.push(M[i][j_]);
			i -= 1;
			j_ += 1;
		}
		res.push(arr);
	}
	let final = [];
	for (let i = 0; i < res.length; i++) {
		const arr = res[i];
		if (i % 2 == 0) {
			final = final.concat(arr.reverse());
		} else {
			final = final.concat(arr);
		}
	}
	return final;
}

// Do not edit the line below.
exports.zigzagTraverse = zigzagTraverse;
