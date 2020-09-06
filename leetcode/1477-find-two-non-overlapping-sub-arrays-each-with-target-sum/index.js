/*
    1st: prefix sum + hashtable + minmax
    - prerequisite: lc560, 915
    - no negative numbers, so the prefixsum is monotonic increasing

    e.g.        [1, 1, 3, 1, 5, 1, 2, 1]
    pfs     ->  [*, *, 2, 2, *, *, *, 3] store the length of subarrays sum to k when we go forward
    prefixs ->  [*, *, 2, 2, 2, 2, 2, 2] store the min length of subarrays when we go forward

    sfs     <-  [*, 2, 2, *, *, 3, *, *] store the length of subarrays sum to k when we go backward
    suffixs <-  [2, 2, 2, 3, 3, 3, *, *] store the min length of subarrays when we go backward

    - Since we only find 2 subarrays, result must be one from left and another from the right
    i.e. res = min(res, prefixs[i] + suffixs[i+1])

    Time    O(5N)
    Space   O(N)
    632 ms, faster than 10.00%
*/
var minSumOfLengths = function (nums, target) {
	const n = nums.length;

	let m = {};
	const pfss = Array(n).fill(Number.MAX_SAFE_INTEGER);
	let pfs = 0;
	for (let i = 0; i < n; i++) {
		pfs += nums[i];
		if (pfs == target) {
			pfss[i] = i + 1;
		}
		const remain = pfs - target;
		if (remain in m) {
			pfss[i] = i - m[remain];
		}
		m[pfs] = i;
		if (i > 0) {
			pfss[i] = Math.min(pfss[i - 1], pfss[i]);
		}
	}

	m = {};
	const sfss = Array(n).fill(Number.MAX_SAFE_INTEGER);
	let sfs = 0;
	for (let i = n - 1; i >= 0; i--) {
		sfs += nums[i];
		if (sfs == target) {
			sfss[i] = n - i;
		}
		const remain = sfs - target;
		if (remain in m) {
			sfss[i] = m[remain] - i;
		}
		m[sfs] = i;
		if (i < n - 1) {
			sfss[i] = Math.min(sfss[i - 1], sfss[i]);
		}
	}

	let res = Number.MAX_SAFE_INTEGER;
	for (let i = 0; i < n - 1; i++) {
		const temp = pfss[i] + sfss[i + 1];
		res = Math.min(res, temp);
	}

	if (res == Number.MAX_SAFE_INTEGER) {
		return -1;
	}
	return res;
};
