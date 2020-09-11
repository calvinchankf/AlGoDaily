/*
    1st: backtracking

    Time    O(N * 3^L) N: number of cells, L: length of target word, 3^L instead of 4^L because we dont go backward
    Space   O(N)
*/
var exist = function (board, word) {
	let R = board.length;
	let C = board[0].length;
	for (let i = 0; i < R; i++) {
		for (let j = 0; j < C; j++) {
			if (word[0] === board[i][j]) {
				let ht = {};
				const b = dfs(board, i, j, word, ht);
				if (b === true) {
					return true;
				}
			}
		}
	}
	return false;
};

const dfs = (board, i, j, word, ht) => {
	if (word.length === 0) {
		return true;
	}
	if (i < 0 || i == board.length || j < 0 || j == board[0].length) {
		return false;
	}
	if (word[0] !== board[i][j]) {
		return false;
	}

	const key = `${i},${j}`;
	if (key in ht) {
		return false;
	}
	ht[key] = true;

	const dirs = [
		[-1, 0],
		[1, 0],
		[0, -1],
		[0, 1],
	];
	for (let [di, dj] of dirs) {
		const b = dfs(board, i + di, j + dj, word.slice(1), ht);
		if (b === true) {
			return true;
		}
	}
	delete ht[key];
	return false;
};

let a = [
	["A", "B", "C", "E"],
	["S", "F", "C", "S"],
	["A", "D", "E", "E"],
];
let b = "ABCCED";
console.log(exist(a, b));

b = "SEE";
console.log(exist(a, b));

b = "ABCB";
console.log(exist(a, b));
