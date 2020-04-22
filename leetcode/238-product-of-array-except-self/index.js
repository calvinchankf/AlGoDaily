/*
    3rd approach: learned from others
	- calculate the products from the front & from the back
		e.g.
								2			3 		4 		5
						->	1		1*2		2*3		2*3*4
							3*4*5	4*5		5*1			1		<-
							-----------------------
			result = 60		20		30			12
	- the cruz of the question is to learn this approach, it is slow but it doesn't matter
	Time	O(3n)
	Space	O(2n)
	76 ms, faster than 89.52%
	8ay2019
*/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
	const n = nums.length;
	const forward = Array(n).fill(1);
	const backward = Array(n).fill(1);
	for (let i = 1; i < n; i++) {
		forward[i] = forward[i - 1] * nums[i - 1];
		const j = n - i - 1;
		backward[j] = backward[j + 1] * nums[j + 1];
	}

	const res = Array(n).fill(1);
	for (let i = 0; i < n; i++) {
		res[i] = forward[i] * backward[i];
	}
	return res;
};
