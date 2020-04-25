/*
    Approach: array
    - keep track of the right-most bulb
    - whenever the right-most bulb equals i + 1 we know all bulbs are blue

    Time    O(N)
    Space   O(1)
    68 ms, faster than 84.05%
*/

/**
 * @param {number[]} light
 * @return {number}
 */
var numTimesAllBlue = function (light) {
	let right = 0;
	let res = 0;
	for (let i = 0; i < light.length; i++) {
		const a = light[i];
		right = Math.max(right, a);
		res += right == i + 1;
	}
	return res;
};
