/*
    1st: backtracking
    - recursively traverse the matrix with dfs
    - to avoid redundant visiting:
        1. temporary put the candidate into the hashtable
        2. remove the candidate after the exploration
        This technique is known as backtacking
    - similar to lc51, 52

    Time    O(RRCC)
    Space   O(RC)
    544 ms, faster than 9.49%
*/
var getMaximumGold = function (grid) {
	let res = 0;
	const dfs = (i, j, ht, gold) => {
		if (i < 0 || i == grid.length || j < 0 || j == grid[i].length) {
			return;
		}
		if (grid[i][j] == 0) {
			return;
		}
		const key = `${i},${j}`;
		if (key in ht) {
			return;
		}
		ht[key] = true;
		gold += grid[i][j];
		res = Math.max(res, gold);

		dfs(i - 1, j, ht, gold);
		dfs(i + 1, j, ht, gold);
		dfs(i, j - 1, ht, gold);
		dfs(i, j + 1, ht, gold);

		delete ht[key];
		return;
	};

	for (let i = 0; i < grid.length; i++) {
		for (let j = 0; j < grid[i].length; j++) {
			if (grid[i][j] != 0) {
				const ht = {};
				dfs(i, j, ht, 0);
			}
		}
	}
	return res;
};
