/*
    1st: backtracking
    Time    O(N * 4^N)
    LTE 135 / 138 test cases passed.
*/
var longestIncreasingPath = function (matrix) {
	if (matrix.length == 0 || matrix[0].length == 0) {
		return 0;
	}

	let maxSteps = 0;
	const R = matrix.length;
	const C = matrix[0].length;

	const dfs = (i, j, hs, steps) => {
		const key = `${i},${j}`;
		if (key in hs) {
			return;
		}
		hs.add(key);

		maxSteps = Math.max(maxSteps, steps);

		const dirs = [
			[-1, 0],
			[1, 0],
			[0, -1],
			[0, 1],
		];
		for (let [di, dj] of dirs) {
			const _i = i + di;
			const _j = j + dj;
			if (_i < 0 || _i == R || _j < 0 || _j == C) {
				continue;
			}
			if (matrix[_i][_j] > matrix[i][j]) {
				dfs(_i, _j, hs, steps + 1);
			}
		}
		hs.delete(key);
		return;
	};

	for (let i = 0; i < R; i++) {
		for (let j = 0; j < C; j++) {
			const hs = new Set();
			dfs(i, j, hs, 1);
		}
	}

	return maxSteps;
};

/*
    2nd: DP
    - it is so similar to lst
    - but we calculate the steps from the bottom to advoid redundant calculation

    Time    O(RC)
    Space   O(RC)
    104 ms, faster than 83.02%
 */
var longestIncreasingPath = function (matrix) {
	if (matrix.length == 0 || matrix[0].length == 0) {
		return 0;
	}

	let maxSteps = 0;
	const R = matrix.length;
	const C = matrix[0].length;
	const ht = [];
	for (let i = 0; i < R; i++) {
		ht.push(Array(C).fill(0));
	}

	const dfs = (i, j) => {
		if (ht[i][j] != 0) {
			return ht[i][j];
		}

		const dirs = [
			[-1, 0],
			[1, 0],
			[0, -1],
			[0, 1],
		];
		for (let [di, dj] of dirs) {
			const _i = i + di;
			const _j = j + dj;
			if (_i < 0 || _i == R || _j < 0 || _j == C) {
				continue;
			}
			if (matrix[_i][_j] > matrix[i][j]) {
				ht[i][j] = Math.max(ht[i][j], dfs(_i, _j));
			}
		}
		ht[i][j] += 1; // this is crucial
		return ht[i][j];
	};

	for (let i = 0; i < R; i++) {
		for (let j = 0; j < C; j++) {
			maxSteps = Math.max(maxSteps, dfs(i, j));
		}
	}

	return maxSteps;
};
