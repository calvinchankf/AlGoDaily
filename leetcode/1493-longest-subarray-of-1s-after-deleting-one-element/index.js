/*
    1st: min max 2 arrays
    - similar to lc42, 135, 487, 915, 1493

    e.g. [0,1,1,0,1,1,1,0]
    ->    0 1 2 0 1 2 3 0
    <-    0 2 1 0 3 2 1 0
    the result is 2(->) + 3(<-)

    Time    O(3N)
    Space   O(2N)
    92 ms, faster than 50.00%
*/
var longestSubarray = function (nums) {
	const n = nums.length;
	const forwards = Array(n).fill(0);
	const backwards = Array(n).fill(0);
	for (let i = 0; i < n; i++) {
		const x = nums[i];
		if (x === 1) {
			const prev = i - 1 >= 0 ? forwards[i - 1] : 0;
			forwards[i] = prev + 1;
		}
	}

	for (let i = n - 1; i >= 0; i--) {
		const x = nums[i];
		if (x === 1) {
			const next = i + 1 < n ? backwards[i + 1] : 0;
			backwards[i] = next + 1;
		}
	}

	let res = 0;
	for (let i = 0; i < n; i++) {
		const prev = i - 1 >= 0 ? forwards[i - 1] : 0;
		const next = i + 1 < n ? backwards[i + 1] : 0;
		res = Math.max(res, prev + next);
	}

	return res;
};
