const shortestRoute = (grid) => {
	const hs = new Set();
	const q = [[0, 0, 0]];
	while (q.length > 0) {
		const [i, j, steps] = q.shift();
		if (i < 0 || i == grid.length || j < 0 || j == grid[0].length) {
			continue;
		}
		if (grid[i][j] === "X") {
			return steps;
		}
		const key = `${i},${j}`;
		if (hs.has(key)) {
			continue;
		}
		hs.add(key);
		if (grid[i][j] === "O") {
			q.push([i - 1, j, steps + 1]);
			q.push([i + 1, j, steps + 1]);
			q.push([i, j - 1, steps + 1]);
			q.push([i, j + 1, steps + 1]);
		}
	}
	return -1;
};

let a = [
	["O", "O", "O", "O"],
	["D", "O", "D", "O"],
	["O", "O", "O", "O"],
	["X", "D", "D", "O"],
];
console.log(shortestRoute(a));
