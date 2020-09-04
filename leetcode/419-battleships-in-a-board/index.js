/*
    1st approach: bfs + hashtable
    - similar to lc200

    Time    O(N)
    Space   O(N)
    136 ms, faster than 6.15%
*/
var countBattleships = function (board) {
	const hs = new Set();
	let res = 0;
	for (let i = 0; i < board.length; i++) {
		for (let j = 0; j < board[0].length; j++) {
			if (board[i][j] == "X" && !hs.has(`${i},${j}`)) {
				bfs(board, i, j, hs);
				res += 1;
			}
		}
	}
	return res;
};

const bfs = (board, x, y, hs) => {
	const q = [[x, y]];
	while (q.length > 0) {
		const [i, j] = q.shift();
		if (i < 0 || i == board.length || j < 0 || j == board[0].length) {
			continue;
		}

		if (board[i][j] == ".") {
			continue;
		}
		const key = `${i},${j}`;
		if (hs.has(key)) {
			continue;
		}
		hs.add(key);

		q.push([i - 1, j]);
		q.push([i + 1, j]);
		q.push([i, j - 1]);
		q.push([i, j + 1]);
	}
};

/*
    2nd approach: bfs
    - mutate the board directly

    TIme    O(n)
    Space   O(1)
    84 ms, faster than 45.25%
*/
var countBattleships = function (board) {
	let res = 0;
	for (let i = 0; i < board.length; i++) {
		for (let j = 0; j < board[0].length; j++) {
			if (board[i][j] == "X") {
				bfs(board, i, j);
				res += 1;
			}
		}
	}
	return res;
};

const bfs = (board, x, y) => {
	const q = [[x, y]];
	while (q.length > 0) {
		const [i, j] = q.shift();
		if (i < 0 || i == board.length || j < 0 || j == board[0].length) {
			continue;
		}

		if (board[i][j] == ".") {
			continue;
		}

		board[i][j] = ".";
		q.push([i - 1, j]);
		q.push([i + 1, j]);
		q.push([i, j - 1]);
		q.push([i, j + 1]);
	}
};

/*
    3rd; to count the start point of every battleship(the top-left corner)

    TIme    O(n)
    Space   O(1)
    80 ms, faster than 62.57%
*/
var countBattleships = function (board) {
	let count = 0;
	for (let i = 0; i < board.length; i++) {
		for (let j = 0; j < board[0].length; j++) {
			if (
				board[i][j] == "X" &&
				(i == 0 || board[i - 1][j] != "X") &&
				(j == 0 || board[i][j - 1] != "X")
			) {
				count++;
			}
		}
	}
	return count;
};
