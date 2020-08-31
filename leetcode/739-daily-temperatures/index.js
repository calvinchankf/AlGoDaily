/*
    1st approach: stack
    
    Time    O(2n)
    Space   O(n)
    192 ms, faster than 58.37%
*/
var dailyTemperatures = function (T) {
	const n = T.length;
	const res = Array(n).fill(0);
	const stack = [];
	for (let i = 0; i < n; i++) {
		const x = T[i];
		while (stack.length > 0 && x > stack[stack.length - 1][0]) {
			const [item, idx] = stack.pop();
			res[idx] = i - idx;
		}
		stack.push([x, i]);
	}
	return res;
};
