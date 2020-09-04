/*
    1st approach: dynamic programming, learned from others
    - the basic idea is that when we pick a color, we should consider add up the cost from previous remaining colors
    e.g. pick red, consider previous cost from green and blue
    
    red = costs[i][0] + min(blue, green)

	- https://www.youtube.com/watch?v=fZIsEPhSBgM&t=1s

	Time	O(N)
	Space	O(3)
	76 ms, faster than 75.68%
*/
var minCost = function (costs) {
	if (costs.length == 0 || costs[0].length == 0) {
		return 0;
	}
	let a = costs[0][0];
	let b = costs[0][1];
	let c = costs[0][2];
	for (let i = 1; i < costs.length; i++) {
		const _a = costs[i][0] + Math.min(b, c);
		const _b = costs[i][1] + Math.min(a, c);
		const _c = costs[i][2] + Math.min(a, b);
		a = _a;
		b = _b;
		c = _c;
	}
	return Math.min(a, b, c);
};
