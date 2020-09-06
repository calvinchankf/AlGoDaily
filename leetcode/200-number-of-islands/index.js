/*
    1st approach: Bfs, hashtable for visited island territories
    
    // 100 ms, faster than 12.22%
*/

/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function (grid) {
	const visited = new Set();
	let res = 0;
	for (let i = 0; i < grid.length; i++) {
		for (let j = 0; j < grid[i].length; j++) {
			const key = i + "," + j;
			if (grid[i][j] == "1" && !visited.has(key)) {
				bfs(grid, i, j, visited);
				res += 1;
			}
		}
	}
	return res;
};

const bfs = (grid, x, y, visited) => {
	const q = [[x, y]];
	while (q.length > 0) {
		const [i, j] = q.shift();
		if (i < 0 || i == grid.length || j < 0 || j == grid[i].length) {
			continue;
		}
		if (grid[i][j] != "1") {
			continue;
		}
		const key = i + "," + j;
		if (visited.has(key)) {
			continue;
		}
		visited.add(key);
		// [
		// 	[-1, 0],
		// 	[1, 0],
		// 	[0, -1],
		// 	[0, 1],
		// ].forEach(([di, dj]) => {
		// 	q.push([i + di, j + dj]);
		// });
		q.push([i - 1, j]);
		q.push([i + 1, j]);
		q.push([i, j - 1]);
		q.push([i, j + 1]);
	}
};
