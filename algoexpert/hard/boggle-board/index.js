function boggleBoard(board, words) {
	// Write your code here.
	const wordSet = new Set(words);
	const res = [];
	for (let w of wordSet) {
		if (exist(board, w)) {
			res.push(w);
		}
	}
	return res;
}

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
		[-1, -1],
		[-1, 1],
		[1, 1],
		[1, -1],
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

// Do not edit the line below.
exports.boggleBoard = boggleBoard;
