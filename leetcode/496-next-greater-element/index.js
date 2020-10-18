/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var nextGreaterElement = function (nums1, nums2) {
	const ht = {};
	const stack = [];
	for (let x of nums2) {
		while (stack.length > 0 && x > stack[stack.length - 1]) {
			const top = stack.pop();
			ht[top] = x;
		}
		stack.push(x);
	}
	const res = [];
	for (let x of nums1) {
		if (x in ht) {
			res.push(ht[x]);
		} else {
			res.push(-1);
		}
	}
	return res;
};
