/**
 * 
 * 1st approach: bfs 
    - need a 2D array. for each cell, calculate the distance from 2s
    - after bfs, if there is still an 1 which the distance is not calculated, return -1

    Time    O(kRC) k=number of rotten oranges in the beginning
    Space   O(RC)
    56 ms, faster than 98.90%
 * 
 * @param {number[][]} grid
 * @return {number}
 */
var orangesRotting = function (grid) {
	const res_arr = [];
	const q = [];
	for (let i = 0; i < grid.length; i++) {
		const temp = [];
		for (let j = 0; j < grid[i].length; j++) {
			temp.push(Number.MAX_SAFE_INTEGER);
			if (grid[i][j] == 2) {
				q.push([i, j, 0]);
			}
		}
		res_arr.push(temp);
	}
	while (q.length > 0) {
		const [i, j, steps] = q.shift();
		if (i < 0 || i === grid.length || j < 0 || j === grid[0].length) {
			continue;
		}
		if (grid[i][j] != 1 && grid[i][j] != 2) {
			continue;
		}
		if (steps < res_arr[i][j]) {
			res_arr[i][j] = steps;
			q.push([i - 1, j, steps + 1]);
			q.push([i + 1, j, steps + 1]);
			q.push([i, j - 1, steps + 1]);
			q.push([i, j + 1, steps + 1]);
		}
	}
	let res = 0;
	for (let i = 0; i < grid.length; i++) {
		for (let j = 0; j < grid[i].length; j++) {
			if (grid[i][j] == 1) {
				if (res_arr[i][j] === Number.MAX_SAFE_INTEGER) {
					return -1;
				}
				res = Math.max(res, res_arr[i][j]);
			}
		}
	}
	return res;
};
