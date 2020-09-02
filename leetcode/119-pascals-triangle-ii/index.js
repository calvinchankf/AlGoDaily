/*
    naive approach

    Time    O(n!)
    Space   O(n)
    84 ms, faster than 29.88%
*/
var getRow = function (rowIndex) {
	let res = [1];
	for (let i = 0; i < rowIndex; i++) {
		const clone = [1];
		for (let j = 0; j < res.length - 1; j++) {
			clone.push(res[j] + res[j + 1]);
		}
		clone.push(1);
		res = clone;
	}
	return res;
};
