/*
    1st approach: sort + binary search
    - sort the intervals (remember the original index by appending to the end, or create a class)
    - for each input interval, binary search to find the interval[j] which start[j] >= end[i]

    Time    O(nlogn)
    Space   O(n)
    128 ms, faster than 74.69%
*/
var findRightInterval = function (intervals) {
	const n = intervals.length;
	const intvs = [];
	for (let i = 0; i < n; i++) {
		const [s, e] = intervals[i];
		intvs.push([s, e, i]);
	}
	intvs.sort((a, b) => a[0] - b[0]);
	const res = [];
	for (let i = 0; i < n; i++) {
		const [s, e] = intervals[i];
		const j = lowerBsearch(intvs, e);
		if (j >= 0 && j < n) {
			const idx = intvs[j][2];
			res.push(idx);
		} else {
			res.push(-1);
		}
	}
	return res;
};

const lowerBsearch = (nums, target) => {
	let left = 0;
	let right = nums.length;
	while (left < right) {
		const mid = Math.floor((left + right) / 2);
		if (target <= nums[mid][0]) {
			right = mid;
		} else {
			left = mid + 1;
		}
	}
	return left;
};
