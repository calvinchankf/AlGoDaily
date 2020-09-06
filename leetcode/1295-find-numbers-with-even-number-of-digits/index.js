/*
    2nd: for each number, divide it by 10 recursively to get the number of digits

    Time    O(NM)
    Space   O(1)
    44 ms, faster than 97.65%
*/
var findNumbers = function (nums) {
	const res = [];
	for (let x of nums) {
		let cur = x;
		let count = 0;
		while (cur > 0) {
			cur = Math.floor(cur / 10);
			count += 1;
		}
		if (count % 2 == 0) {
			res.push(x);
		}
	}
	return res.length;
};
