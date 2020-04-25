/*
    1st approach: sort + 2 pointers
    - 2 sum closest

    Time    O(nlogn)
    Space   O(1)
    32 ms, faster than 67.83%
*/
var twoSumLessThanK = function (A, K) {
	A.sort((a, b) => a - b);
	let i = 0;
	let j = A.length - 1;

	let cur = -1;
	while (i < j) {
		const total = A[i] + A[j];
		if (total < K && Math.abs(total - K) < Math.abs(cur - K)) {
			cur = total;
		} else {
			if (total < K) {
				i += 1;
			} else {
				j -= 1;
			}
		}
	}
	return cur;
};
