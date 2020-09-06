function riverSizes(matrix) {
	// Write your code here.
	const R = matrix.length;
	const C = matrix[0].length;
	const res = [];
	const ht = {};
	for (let i = 0; i < R; i++) {
		for (let j = 0; j < C; j++) {
			if (matrix[i][j] == 1 && ht[`${i},${j}`] == undefined) {
				const area = bfs(matrix, i, j, ht);
				res.push(area);
			}
		}
	}
	return res;
}
const bfs = (matrix, x, y, ht) => {
	const R = matrix.length;
	const C = matrix[0].length;
	let area = 0;
	const q = [[x, y]];
	while (q.length > 0) {
		const [i, j] = q.shift();
		if (i < 0 || i == R || j < 0 || j == C) {
			continue;
		}
		if (matrix[i][j] == 0) {
			continue;
		}
		const key = `${i},${j}`;
		if (key in ht) {
			continue;
		}
		ht[key] = true;

		area += 1;
		q.push([i - 1, j]);
		q.push([i + 1, j]);
		q.push([i, j - 1]);
		q.push([i, j + 1]);
	}
	return area;
};

// Do not edit the line below.
exports.riverSizes = riverSizes;
