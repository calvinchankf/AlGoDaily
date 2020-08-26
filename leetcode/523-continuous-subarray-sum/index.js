/*
    2nd: zero sum subarray
    - similar to lc325, 525, 560, 930, 1124, 1171

    Time    O(N)
    Space   O(N)
    84 ms, faster than 76.47% 
*/
var checkSubarraySum = function (nums, k) {
	const ht = {};
	let pfs = 0;
	for (let i = 0; i < nums.length; i++) {
		const x = nums[i];
		pfs += x;
		if (k != 0) {
			pfs = pfs % k;
		}
		if (pfs == 0 && i > 0) {
			return true;
		}
		if (pfs in ht && i - ht[pfs] > 1) {
			return true;
		}
		if (ht[pfs] === undefined) {
			ht[pfs] = i;
		}
	}
	return false;
};
