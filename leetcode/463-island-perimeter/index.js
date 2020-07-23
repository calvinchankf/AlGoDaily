/*
    1st approach: recursive dfs, combine the perimeter of each grid
    - simiar to lc1020, lc1254

    Time    O(n)
    Space   O(n, d)
    376 ms, faster than 6.47%
*/
var islandPerimeter = function (grid) {
	if (grid.length == 0 || grid[0].length == 0) {
		return 0;
	}
	const r = grid.length;
	const c = grid[0].length;
	const seen = {};
	for (let i = 0; i < r; i++) {
		for (let j = 0; j < c; j++) {
			const key = `${i},${j}`;
			if (grid[i][j] === 1 && seen[key] === undefined) {
				return dfs(grid, i, j, seen);
			}
		}
	}
	return 0;
};

var dfs = function (grid, i, j, seen) {
	if (i < 0 || i == grid.length || j < 0 || j == grid[0].length) {
		return 1;
	}
	if (grid[i][j] === 0) {
		return 1;
	}
	const key = `${i},${j}`;
	if (key in seen) {
		return 0;
	}
	seen[key] = true;
	let total = 0;
	total += dfs(grid, i - 1, j, seen);
	total += dfs(grid, i + 1, j, seen);
	total += dfs(grid, i, j - 1, seen);
	total += dfs(grid, i, j + 1, seen);
	return total;
};
