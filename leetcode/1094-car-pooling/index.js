/*
    1st: math
    - similar to lc1109, 1589
    - typical range counting technique to deal with values on a range
    - basically we can just use the prefix-sum concept to mark the start and the end of each interval

    Time    O(2n)
    Space   O(n)
    84 ms, faster than 76.38%
*/
var carPooling = function (trips, capacity) {
	let n = 0;
	for (let [c, i, j] of trips) {
		n = Math.max(n, j);
	}
	const occupiedCounts = Array(n + 1).fill(0);
	for (let [c, i, j] of trips) {
		occupiedCounts[i] += c;
		occupiedCounts[j] -= c;
	}
	for (let i = 1; i < n + 1; i++) {
		occupiedCounts[i] += occupiedCounts[i - 1];
	}
	let maxCount = 0;
	for (let i = 0; i < n + 1; i++) {
		maxCount = Math.max(maxCount, occupiedCounts[i]);
	}
	return maxCount <= capacity;
};
