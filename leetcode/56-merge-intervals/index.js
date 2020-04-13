/*
    1st approach: sort
    1. sort the intervals by start time
    2. iterate the intervals and compare the cur interval start time with the last interval end time

    Time    O(nlogn)
    Space   O(n)
    88 ms, faster than 24.16%
    20apr2019
*/

/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function (intervals) {
	if (intervals.length == 0) {
		return [];
	}
	intervals = intervals.sort((a, b) => {
		if (a[0] == b[0]) {
			return a[1] - b[1];
		}
		return a[0] - b[0];
	});
	const res = [intervals[0]];
	for (let i = 0; i < intervals.length; i++) {
		const lastIdx = res.length - 1;
		intv = intervals[i];
		if (intv[0] <= res[lastIdx][1]) {
			res[lastIdx][1] = Math.max(res[lastIdx][1], intv[1]);
		} else {
			res.push(intv);
		}
	}
	return res;
};
