/*
    1st: brute-force + sort

    Time    O(XlogX) X = N^2
    Space   O(N^2)
    428 ms, faster than 50.00%
*/
var rangeSum = function (nums, n, left, right) {
	const cands = [];
	for (let i = 0; i < nums.length; i++) {
		let total = 0;
		for (let j = i; j < nums.length; j++) {
			total += nums[j];
			cands.push(total);
		}
	}
	cands.sort((a, b) => a - b);
	let res = 0;
	for (let i = left - 1; i < right && i < cands.length; i++) {
		res += cands[i] % (Math.pow(10, 9) + 7);
	}
	return res;
};
