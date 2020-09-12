/*
    1st: reuse thr logic of calculatorIII
    LTE
*/
var calculate = function (s) {
	const q = s.split("");
	return helper(q);
};

var helper = function (q) {
	let sign = "+";
	let num = 0;
	const stack = [];
	while (q.length > 0) {
		const c = q.shift();

		if ("0123456789".indexOf(parseInt(c)) > -1) {
			num = num * 10 + parseInt(c);
		} else if (c == "(") {
			num = helper(q);
		}
		if (q.length == 0 || "+-*/)".indexOf(c) > -1) {
			if (sign == "+") {
				stack.push(num);
			} else if (sign == "-") {
				stack.push(-num);
			} else if (sign == "*") {
				const n = stack.length;
				stack[n - 1] = stack[n - 1] * num;
			} else if (sign == "/") {
				const n = stack.length;
				// in js, -3/2 = -2,
				// but the question wants "The integer division should truncate toward zero"
				// so should be -3/2 = -1
				const isNegative = stack[n - 1] < 0;
				const temp = Math.abs(stack[n - 1]);
				stack[n - 1] = Math.floor(temp / num);
				if (isNegative) {
					stack[n - 1] = -stack[n - 1];
				}
			}
			sign = c;
			num = 0;
			if (sign == ")") {
				break;
			}
		}
	}
	let res = 0;
	for (let num of stack) {
		res += num;
	}
	return res;
};
