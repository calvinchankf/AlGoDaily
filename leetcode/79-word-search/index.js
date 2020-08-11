/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function (board, word) {
	let R = board.length;
	let C = board[0].length;
	for (let i = 0; i < R; i++) {
		for (let j = 0; j < C; j++) {
			// console.log(i, j, word[0], board[i][j]);
			if (word[0] === board[i][j]) {
				let hs = new Set();
				const b = dfs(board, i, j, word, hs);
				if (b === true) {
					return true;
				}
			}
		}
	}
	return false;
};

const dfs = (board, i, j, word, hs) => {
	if (word.length === 0) {
		return true;
	}

	// console.log(i, j, word, hs);

	if (i < 0 || i == board.length || j < 0 || j == board[0].length) {
		return false;
	}

	if (word[0] !== board[i][j]) {
		return false;
	}

	const key = `${i},${j}`;
	if (hs.has(key)) {
		return false;
	}
	hs.add(key);

	const dirs = [
		[-1, 0],
		[1, 0],
		[0, -1],
		[0, 1],
	];
	for (let [di, dj] of dirs) {
		const b = dfs(board, i + di, j + dj, word.slice(1), hs);
		if (b === true) {
			return true;
		}
		// hs.delete(`${i + di},${j + dj}`);
	}
	hs.delete(key);
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
