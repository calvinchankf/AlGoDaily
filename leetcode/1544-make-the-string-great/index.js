/*
    1st: stack

    Time    O(N)
    Space   O(N)
    72 ms, faster than 100.00%
*/
var makeGood = function (s) {
	const stack = [];
	for (let c of s) {
		if (
			stack.length > 0 &&
			c !== stack[stack.length - 1] &&
			c.toLowerCase() === stack[stack.length - 1].toLowerCase()
		) {
			stack.pop();
		} else {
			stack.push(c);
		}
	}
	return stack.join("");
};
