/*
    2nd: sort
    - merge the intervals
    - put the intersections into the result array

    Time    O(NlogN) N=A+B
    Space   O(N)
    104 ms, faster than 71.83% 
*/
var intervalIntersection = function (A, B) {
	let intvs = A.concat(B);
	intvs.sort((a, b) => {
		if (a[0] == b[0]) {
			return a[1] - b[1];
		}
		return a[0] - b[0];
	});

	const res = [];
	const mergeds = [intvs[0]];
	for (let i = 1; i < intvs.length; i++) {
		const [s, e] = intvs[i];
		const n = mergeds.length;
		if (s <= mergeds[n - 1][1]) {
			res.push([s, Math.min(mergeds[n - 1][1], e)]);
			mergeds[n - 1][1] = Math.max(mergeds[n - 1][1], e);
		} else {
			mergeds.push([s, e]);
		}
	}
	return res;
};
