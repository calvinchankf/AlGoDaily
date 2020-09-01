/*
    1st approach: BFS + hashset
    - on each cell, BFS to traverse in 9 directions
    - use a hashset to avoid redundant visit

    Time    O(RC)
    Space   O(RC)
    280 ms, faster than 15.03%
*/
var shortestPathBinaryMatrix = function (grid) {
	const R = grid.length;
	const C = grid[0].length;
	const hs = new Set();
	const q = [[0, 0, 1]];

	const dirs = [
		[-1, -1],
		[-1, 0],
		[-1, 1],
		[0, 1],
		[1, 1],
		[1, 0],
		[1, -1],
		[0, -1],
	];

	while (q.length > 0) {
		const [i, j, steps] = q.shift();
		if (i < 0 || i == R || j < 0 || j == C) {
			continue;
		}
		if (i + 1 == R && j + 1 == C) {
			if (grid[i][j] == 0) {
				return steps;
			}
			return -1;
		}
		if (grid[i][j] == 1) {
			continue;
		}

		const key = `${i},${j}`;
		if (hs.has(key)) {
			continue;
		}
		hs.add(key);

		for (let [di, dj] of dirs) {
			q.push([i + di, j + dj, steps + 1]);
		}
	}

	return -1;
};
