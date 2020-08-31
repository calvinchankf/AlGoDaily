/*
    1st: math

    Time    O(1)
    Space   O(1)
    76 ms, faster than 46.34%
*/
var numMovesStones = function (a, b, c) {
	const max = Math.max(a, b, c);
	const min = Math.min(a, b, c);
	let mid = null;
	for (let x of [a, b, c]) {
		if (x !== min && x !== max) {
			mid = x;
		}
	}
	const leftUnoccupied = mid - min - 1;
	const rightUnoccupied = max - mid - 1;
	const minTargetRange = Math.min(leftUnoccupied, rightUnoccupied);
	const maxTargetRange = Math.max(leftUnoccupied, rightUnoccupied);
	let minMoves = 0;
	if (minTargetRange <= 1 && maxTargetRange > 0) {
		minMoves = 1;
	} else if (maxTargetRange > 0) {
		minMoves = 2;
	}
	const maxMoves = leftUnoccupied + rightUnoccupied;
	return [minMoves, maxMoves];
};
/*
    2nd: same as 1st but cleaner

    Time    O(1) <- 3log3 ~= 3
    Space   O(1)
    108 ms, faster than 9.76% <- extra time is used becos of the array declaration and sort
*/
var numMovesStones = function (a, b, c) {
	const A = [a, b, c].sort((a, b) => a - b);
	if (A[2] - A[0] == 2) {
		return [0, 0];
	}
	const leftUnoccupied = A[1] - A[0] - 1;
	const rightUnoccupied = A[2] - A[1] - 1;
	const minTargetRange = Math.min(leftUnoccupied, rightUnoccupied);
	let minMoves = 2;
	if (minTargetRange <= 1) {
		minMoves = 1;
	}
	const maxMoves = leftUnoccupied + rightUnoccupied;
	return [minMoves, maxMoves];
};
