/*
    2nd approach
	- iterative bfs
	- when we see an one, bfs its neightbours to calculate its area and compare to the potential result
	- if it is larger than the potential result, set it as the potential result

	Time    O(n)
	Space   O(n) hashtable
	152 ms, faster than 15.95%
*/
var maxAreaOfIsland = function (grid) {
	const R = grid.length;
	const C = grid[0].length;

	if (R == 0 || C == 0) {
		return 0;
	}

	let res = 0;
	const ht = {};
	for (let i = 0; i < R; i++) {
		for (let j = 0; j < C; j++) {
			const key = `${i},${j}`;
			if (grid[i][j] == 1) {
				const area = bfs(grid, i, j, ht);
				res = Math.max(res, area);
			}
		}
	}
	return res;
};

const bfs = (grid, x, y, ht) => {
	const R = grid.length;
	const C = grid[0].length;

	let area = 0;
	const q = [[x, y]];
	while (q.length > 0) {
		const [i, j] = q.shift();
		if (i < 0 || i == R || j < 0 || j == C) {
			continue;
		}
		if (grid[i][j] == 0) {
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
