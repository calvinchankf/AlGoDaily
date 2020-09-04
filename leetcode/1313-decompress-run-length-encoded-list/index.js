/*
    very bad description

    Time    O(N)
    Space   O(N)
    68 ms, faster than 99.92%
*/
var decompressRLElist = function (nums) {
	const res = [];
	let i = 0;
	while (i < nums.length) {
		const freq = nums[i];
		const val = nums[i + 1];
		for (let j = 0; j < freq; j++) {
			res.push(val);
		}
		i += 2;
	}
	return res;
};
