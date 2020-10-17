/*
    1st approach:
    - similar to lc56, 252, 253, 435, 452, 646
	1. sort the intervals by start time
	2. prepare a temporary array for nonoverlapping intervals
	3. when the current interval follows(behind and not overlap) the temp array last item, append to the temp array
	4. when the current interval overlaps but shorter than the temp array last item, replace the temp array last item, res++
	5. when the current interval overlaps with the previous interval, res++

    corner case: [[1,10], [2,3], [3,4], [4,5], [5,6], [7,8]]
    we should just remove the [1, 10]

	Time		O(nlogn)    built-in sort
	Space		O(n)		the temporary array
    80 ms, faster than 65.43%
*/
var eraseOverlapIntervals = function (intervals) {
	intervals.sort((a, b) => {
		if (a[0] == b[0]) {
			return a[1] - b[1];
		}
		return a[0] - b[0];
	});
	let res = 0;
	const mergeds = [intervals[0]];
	for (let i = 1; i < intervals.length; i++) {
		const [s, e] = intervals[i];
		const n = mergeds.length;
		if (s < mergeds[n - 1][1]) {
			if (e < mergeds[n - 1][1]) {
				mergeds[n - 1] = [s, e];
			}
			res += 1;
		} else {
			mergeds.push([s, e]);
		}
	}
	return res;
};

/*
    2nd: space optimization

    Time    O(NlogN)
    Space   O(1)
    80 ms, faster than 65.43%
*/
var eraseOverlapIntervals = function (intervals) {
	if (intervals.length == 0) {
		return [];
	}
	intervals.sort((a, b) => {
		if (a[0] == b[0]) {
			return a[1] - b[1];
		}
		return a[0] - b[0];
	});
	let res = 0;
	let maxEnd = intervals[0][1];
	for (let i = 1; i < intervals.length; i++) {
		const [s, e] = intervals[i];
		if (s < maxEnd) {
			if (e < maxEnd) {
				maxEnd = e;
			}
			res += 1;
		} else {
			maxEnd = e;
		}
	}
	return res;
};
