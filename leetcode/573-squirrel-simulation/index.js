/*
    Math
    - i am not good at math, i learned from others
    - accumulate the distance from nuts to the tree
    - see which total distance is the smallest

    ref:
    - https://leetcode.com/problems/squirrel-simulation/discuss/102819/Python-Straightforward-with-Explanation

    Time    O(N)
    Space   O(1)
    116 ms, faster than 43.75%
*/
var minDistance = function (height, width, tree, squirrel, nuts) {
	let total = 0;
	// accumulate the distance from nuts to the tree
	for (let nut of nuts) {
		total += 2 * manhattan(nut, tree);
	}
	// just to see which total distance is the smallest
	let res = Number.MAX_SAFE_INTEGER;
	for (let nut of nuts) {
		const temp = total + manhattan(squirrel, nut) - manhattan(nut, tree);
		if (temp < res) {
			res = temp;
		}
	}
	return res;
};

const manhattan = (a, b) => {
	return Math.abs(a[0] - b[0]) + Math.abs(a[1] - b[1]);
};
