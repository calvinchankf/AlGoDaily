/*
    1st approach
    - sort the array, compare the item[i].start and item[i-1].end
    
    Time	    O(nlogn)
    Space	    O(1)
    76 ms, faster than 39.42%
*/
var canAttendMeetings = function (intervals) {
	intervals.sort((a, b) => a[0] - b[0]);
	let maxEnd = Number.MIN_SAFE_INTEGER;
	for (let [s, e] of intervals) {
		if (s < maxEnd) {
			return false;
		}
		maxEnd = e;
	}
	return true;
};
