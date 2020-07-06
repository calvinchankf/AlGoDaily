/*
    1st: observation
    - after observation, we found out that the cells pattern repeat for every 15 iterations

    Time    O(14*8) -> O(1)
    Space   O(8)
    24 ms, faster than 100.00%
*/
var prisonAfterNDays = function (cells, N) {
	let n = N % 14;
	if (n == 0) {
		n = 14;
	}
	let newCells = [-1, ...cells, -1];
	for (let i = 0; i < n; i++) {
		const clone = [...newCells];
		for (let j = 1; j < newCells.length - 1; j++) {
			clone[j] = newCells[j - 1] === newCells[j + 1] ? 1 : 0;
		}
		newCells = clone;
	}
	return newCells.slice(1, newCells.length - 1);
};
