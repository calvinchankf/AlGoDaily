/*
    2nd: BFS

    Time    O(2n)
    Space   O(n) hashtable
    176 ms, faster than 6.93%
*/
/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solve = function (board) {
	const touched = new Set();

	for (let i = 0; i < board.length; i++) {
		for (let j = 0; j < board[0].length; j++) {
			if (!touched.has(`${i},${j}`) && board[i][j] === "O") {
				const b = ifTouchBoundary(board, i, j, touched);
				if (b === false) {
					capture(board, i, j);
				}
			}
		}
	}
};

const ifTouchBoundary = (board, x, y, touched) => {
	const seen = new Set();
	const q = [[x, y]];
	while (q.length > 0) {
		const [i, j] = q.shift();
		if (i < 0 || i === board.length || j < 0 || j === board[0].length) {
			return true;
		}
		if (board[i][j] === "O") {
			const key = `${i},${j}`;

			if (seen.has(key)) {
				continue;
			}
			seen.add(key);

			if (touched.has(key)) {
				return true;
			}
			touched.add(key);

			q.push([i - 1, j]);
			q.push([i + 1, j]);
			q.push([i, j - 1]);
			q.push([i, j + 1]);
		}
	}
	return false;
};

const capture = (board, i, j) => {
	if (i < 0 || i === board.length || j < 0 || j === board[0].length) {
		return;
	}
	if (board[i][j] == "O") {
		board[i][j] = "X";
		capture(board, i - 1, j);
		capture(board, i + 1, j);
		capture(board, i, j - 1);
		capture(board, i, j + 1);
	}
};
