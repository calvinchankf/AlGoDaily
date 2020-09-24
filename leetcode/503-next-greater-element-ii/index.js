/*
    2nd classic approach: stack
	- classic approach: https://www.youtube.com/watch?v=uFso48YRRao
	- [for duplicates]save the index of a number as well, [num, i], into stack, such that we can know which number it refers to

	Time		O(n)
	Space		O(n)
	116 ms, faster than 78.76%
*/
var nextGreaterElements = function (nums) {
	const arr = nums.concat(nums);
	const n = arr.length;
	const res = Array(n).fill(-1);
	const stack = [];
	for (let i = 0; i < n; i++) {
		const x = arr[i];
		while (stack.length > 0 && arr[stack[stack.length - 1]] < arr[i]) {
			const j = stack.pop();
			res[j] = x;
		}
		stack.push(i);
	}
	return res.slice(0, n / 2);
};
