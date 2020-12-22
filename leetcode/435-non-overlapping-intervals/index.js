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

/*
    2nd: activity selection
    - similar to 435, 646
    - sort by end time
    - update the count & curEnd greedily

    Time    O(NlogN)
    Space   O(1)
    84 ms, faster than 62.50%
*/
var eraseOverlapIntervals = function(intervals) {
    if (intervals.length == 0) { return 0 }
    intervals.sort((a, b) => a[1] - b[1])
    let curEnd = -(2**32)
    let legitCount = 0
    for (let [s, e] of intervals) {
        if (s >= curEnd) {
            curEnd = e
            legitCount += 1
        }
    }
    return intervals.length - legitCount
};