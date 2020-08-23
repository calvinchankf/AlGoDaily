/*
    1st approach: BFS
    - similar to lc505, 562
    - if the ball hits the wall, try to roll in 4 directions until the explorations hit the wall
    - only cache the pivot points where we turned(in front of the wall)

    Time    O(RC)
    Space    O(RC)
    128 ms, faster than 28.10%
*/
var hasPath = function (maze, start, destination) {
	const R = maze.length;
	const C = maze[0].length;
	const hs = new Set();
	const dirs = [
		[-1, 0],
		[1, 0],
		[0, -1],
		[0, 1],
	];
	const q = [start];

	while (q.length > 0) {
		const [i, j] = q.shift();
		const key = `${i},${j}`;
		if (hs.has(key)) {
			continue;
		}
		hs.add(key);
		if (i == destination[0] && j == destination[1]) {
			return true;
		}
		for (let [di, dj] of dirs) {
			let _i = i;
			let _j = j;
			while (
				_i + di >= 0 &&
				_i + di < R &&
				_j + dj >= 0 &&
				_j + dj < C &&
				maze[_i + di][_j + dj] == 0
			) {
				_i += di;
				_j += dj;
			}
			q.push([_i, _j]);
		}
	}
	return false;
};
