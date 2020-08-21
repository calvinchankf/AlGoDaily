/*
    2nd: min max 2 arrays
    - similar to lc915
    - from the front to the end, store the number of candies by comparing with the previous item
    - from the end to the front, store the number of candies by comparing with the previous item
    - the max of forwards[i] and backwards[i] is our result at each index

    e.g. 12, 4, 3, 11, 34, 34, 67
    ->    1, 1, 1,  2,  3,  1,  2
    <-    3, 2, 1,  1,  1,  1,  1
    -----------------------------
    max   3, 2, 1,  2,  3,  1,  2

    Time    O(3N)
    Space   O(2N)
    100 ms, faster than 42.70%
*/
var candy = function (ratings) {
	const n = ratings.length;
	const forwards = Array(n).fill(1);
	const backwards = Array(n).fill(1);
	for (let i = 1; i < n; i++) {
		if (ratings[i] > ratings[i - 1]) {
			forwards[i] = forwards[i - 1] + 1;
		}
	}
	for (let i = n - 1; i >= 0; i--) {
		if (ratings[i] > ratings[i + 1]) {
			backwards[i] = backwards[i + 1] + 1;
		}
	}
	let res = 0;
	for (let i = 0; i < n; i++) {
		res += Math.max(forwards[i], backwards[i]);
	}
	return res;
};
