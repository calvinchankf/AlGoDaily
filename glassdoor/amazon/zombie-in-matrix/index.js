/*
    Given a 2D grid, each cell is either a zombie 1 or a human 0. 
    Zombies can turn adjacent (up/down/left/right) human beings into zombies every hour. 
    Find out how many hours does it take to infect all humans?

    Input:
    [[0, 1, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0]]

    Output: 2

    Explanation:
    At the end of the 1st hour, the status of the grid:
    [[1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 1, 0, 1, 1],
    [1, 1, 1, 0, 1]]

    At the end of the 2nd hour, the status of the grid:
    [[1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]]
*/

var zombieInMatrix = function (grid) {
	const distances = [];
	const q = [];
	for (let i = 0; i < grid.length; i++) {
		const temp = [];
		for (let j = 0; j < grid[i].length; j++) {
			temp.push(Number.MAX_SAFE_INTEGER);
			if (grid[i][j] == 1) {
				q.push([i, j, 0]);
			}
		}
		distances.push(temp);
	}
	while (q.length > 0) {
		const [i, j, steps] = q.shift();
		if (i < 0 || i === grid.length || j < 0 || j === grid[0].length) {
			continue;
		}
		if (steps < distances[i][j]) {
			distances[i][j] = steps;
			q.push([i - 1, j, steps + 1]);
			q.push([i + 1, j, steps + 1]);
			q.push([i, j - 1, steps + 1]);
			q.push([i, j + 1, steps + 1]);
		}
	}
	let res = 0;
	for (let i = 0; i < grid.length; i++) {
		for (let j = 0; j < grid[i].length; j++) {
			if (grid[i][j] == 0) {
				res = Math.max(res, distances[i][j]);
			}
		}
	}
	return res;
};

a = [
	[0, 1, 1, 0, 1],
	[0, 1, 0, 1, 0],
	[0, 0, 0, 0, 1],
	[0, 1, 0, 0, 0],
];
console.log(zombieInMatrix(a));
