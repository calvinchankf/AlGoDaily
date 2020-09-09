/**
 * Initialize your data structure here.
 * @param {number} n
 */
var TicTacToe = function (n) {
	this.board = [];
	for (let i = 0; i < n; i++) {
		this.board.push(Array(n).fill(0));
	}
};

/**
 * Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins. 
 * @param {number} row 
 * @param {number} col 
 * @param {number} player
 * @return {number}
 */
TicTacToe.prototype.move = function (row, col, player) {
	const n = this.board.length;
	this.board[row][col] = player;

	// row
	let count = 0;
	for (let i = 0; i < n; i++) {
		if (this.board[i][col] == player) {
			count += 1;
		}
	}
	if (count == n) {
		return player;
	}

	// col
	count = 0;
	for (let j = 0; j < n; j++) {
		if (this.board[row][j] == player) {
			count += 1;
		}
	}
	if (count == n) {
		return player;
	}

	// diag
	count = 0;
	for (let d = 0; d < n; d++) {
		if (this.board[d][d] == player) {
			count += 1;
		}
	}
	if (count == n) {
		return player;
	}

	// anti - diag
	count = 0;
	for (let d = 0; d < n; d++) {
		if (this.board[d][n - d - 1] == player) {
			count += 1;
		}
	}
	if (count == n) {
		return player;
	}

	return 0;
};

/**
 * Your TicTacToe object will be instantiated and called as such:
 * var obj = new TicTacToe(n)
 * var param_1 = obj.move(row,col,player)
 */
