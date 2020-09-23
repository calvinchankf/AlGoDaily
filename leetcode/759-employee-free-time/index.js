/**
 * // Definition for an Interval.
 * function Interval(start, end) {
 *    this.start = start;
 *    this.end = end;
 * };
 */

/*
    1st approach: heap + merge intervals
    1. put all the intervals together and sort them
    2. merge the intervals
    3. the result is essentially the list of the gaps between the merged intervals

    Time    O(nlogn) n: number of intervals
    Space   O(n)
    104 ms, faster than 74.02%
*/
var employeeFreeTime = function (schedule) {
	let intvs = [];
	for (let arr of schedule) {
		intvs = intvs.concat(arr);
	}
	intvs.sort((a, b) => {
		if (a.start == b.start) {
			return a.end - b.end;
		}
		return a.start - b.start;
	});

	const mergeds = [intvs[0]];
	for (let i = 1; i < intvs.length; i++) {
		const { start, end } = intvs[i];
		const n = mergeds.length;
		if (start < mergeds[n - 1].end) {
			mergeds[n - 1].end = Math.max(mergeds[n - 1].end, end);
		} else {
			mergeds.push(intvs[i]);
		}
	}

	const res = [];
	for (let i = 1; i < mergeds.length; i++) {
		const prevEnd = mergeds[i - 1].end;
		const curStart = mergeds[i].start;
		const diff = curStart - prevEnd;
		if (diff > 0) {
			res.push(new Interval(prevEnd, curStart));
		}
	}
	return res;
};
