/*
    2nd: 2 arrays min max
    - similar to lc42, 135, 915, 1493

    Time    O(N)
    Space   O(N)
    92 ms, faster than 46.71%
*/
var findMaxConsecutiveOnes = function (nums) {
	const n = nums.length;
	if (n == 0) {
		return 0;
	}
	const forwards = Array(n).fill(0);
	for (let i = 0; i < n; i++) {
		if (nums[i] == 1) {
			forwards[i] = 1 + (i - 1 >= 0 ? forwards[i - 1] : 0);
		}
	}
	const backwards = Array(n).fill(0);
	for (let i = n - 1; i >= 0; i--) {
		if (nums[i] == 1) {
			backwards[i] = 1 + (i + 1 < n ? backwards[i + 1] : 0);
		}
	}
	let res = 0;
	for (let i = 0; i < n; i++) {
		if (nums[i] == 0) {
			const total =
				1 +
				(i - 1 >= 0 ? forwards[i - 1] : 0) +
				(i + 1 < n ? backwards[i + 1] : 0);
			res = Math.max(res, total);
		}
	}
	if (res == 0) {
		return forwards[n - 1];
	}
	return res;
};
