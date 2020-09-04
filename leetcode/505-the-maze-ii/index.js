/*
    1st approach: BFS
    - similar to lc490, 562
    - we need a 2D array to cache the min distance on each cell !!!!
    - if the ball hits the wall, try to roll in 4 directions until the explorations hit the wall
    - only cache the pivot points where we turned(in front of the wall)

    Time    O(RCmax(R,C)) for every point, we can traverse up to R or C depth
    Space    O(RC)
    124 ms, faster than 77.36%
*/
var shortestDistance = function (maze, start, destination) {
	const R = maze.length;
	const C = maze[0].length;
	const ht = {};
	const dirs = [
		[-1, 0],
		[1, 0],
		[0, -1],
		[0, 1],
	];
	const q = [[start[0], start[1], 0]];

	while (q.length > 0) {
		const [i, j, steps] = q.shift();

		const key = `${i},${j}`;
		if (steps >= ht[key]) {
			continue;
		}
		ht[key] = steps; // so now we have a shorter prefix path

		if (i == destination[0] && j == destination[1]) {
			continue;
		}

		for (let [di, dj] of dirs) {
			let _i = i;
			let _j = j;
			let count = 0;
			while (
				_i + di >= 0 &&
				_i + di < R &&
				_j + dj >= 0 &&
				_j + dj < C &&
				maze[_i + di][_j + dj] == 0
			) {
				_i += di;
				_j += dj;
				count += 1;
			}
			q.push([_i, _j, steps + count]);
		}
	}
	const key = `${destination[0]},${destination[1]}`;
	if (key in ht) {
		return ht[key];
	}
	return -1;
};
