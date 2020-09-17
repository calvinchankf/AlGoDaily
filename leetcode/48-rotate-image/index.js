var rotate = function (matrix) {
	const n = matrix.length;

	// transpose
	for (let i = 0; i < n; i++) {
		for (let j = 0; j < i; j++) {
			[matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]];
		}
	}

	// swap columns on each row
	for (let i = 0; i < n; i++) {
		for (let j = 0; j < Math.floor(n / 2); j++) {
			[matrix[i][j], matrix[i][n - j - 1]] = [
				matrix[i][n - j - 1],
				matrix[i][j],
			];
		}
	}
};
